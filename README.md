# DAE - Laboratorio 04

## Relación de Modelos en Django

En este laboratorio se trabajó con las relaciones entre modelos en Django, utilizando una aplicación de biblioteca para representar diferentes tipos de relaciones entre autores, libros, categorías y editoriales.

## Descripción

El proyecto permite gestionar información relacionada con libros y comprobar el funcionamiento de las relaciones entre modelos de Django.

Se implementaron las siguientes relaciones:

- `ForeignKey`: relación entre `Book` y `Author`.
- `OneToOneField`: relación entre `Author` y `AuthorProfile`.
- `ManyToManyField`: relación entre `Book` y `Category`.
- `ManyToManyField` con `through`: relación entre `Book` y `Publisher` mediante el modelo intermedio `Publication`.

El modelo `Publication` permite almacenar información adicional de la relación, como la fecha de publicación y la edición.

## Modelos

- Author
- AuthorProfile
- Book
- Category
- Publisher
- Publication

## Funcionalidades realizadas

- Creación de modelos relacionados.
- Generación y aplicación de migraciones.
- Registro de datos mediante Django Admin.
- Consultas de relaciones desde Django Shell.
- Consultas directas e inversas entre modelos.
- Uso de filtros con doble guion bajo.
- Comprobación del comportamiento de `on_delete`.
- Visualización del detalle de un libro con su autor, categorías y editorial.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- Pillow
- HTML
- Git y GitHub

## Ejecución del proyecto

Instalar las dependencias:

```bash
pip install -r requirements.txt
