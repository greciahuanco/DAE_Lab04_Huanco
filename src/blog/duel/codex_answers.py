"""Additional Codex proposal; retained separately for comparison."""
from datetime import date

from django.db.models import Count, Exists, OuterRef

from blog.models import Author, Comment, Post


def q1():
    return Post.objects.filter(published=True)


def q2():
    return Post.objects.filter(category=None)


def q3():
    return Post.objects.filter(
        published_at__gte=date(2026, 3, 1),
        published_at__lte=date(2026, 5, 31),
    )


def q4():
    return Post.objects.annotate(total=Count("comments")).filter(total__gt=2)


def q5():
    return (
        Post.objects.filter(published=True)
        .annotate(
            n_comments=Count("comments", distinct=True),
            n_tags=Count("tags", distinct=True),
        )
        .order_by("-n_comments", "pk")[:3]
    )


def q6():
    return Post.objects.filter(author__profile__country="Perú")


def q7():
    return Comment.objects.filter(post__category__name="Tecnología")


def q8():
    published = Post.objects.filter(author_id=OuterRef("pk"), published=True)
    return Author.objects.filter(~Exists(published))
