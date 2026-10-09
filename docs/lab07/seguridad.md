# Puntos 12 a 14 Frontera de confianza

Se ejecutaron las cuatro intenciones del README:
posts_per_author y comments_of_post devolvieron ok;
delete_comments_of_post devolvió approval_required y run_sql devolvió denied.
Los registros 16 contienen las respuestas completas.

El cuarto comentario del artículo 1 pide ignorar instrucciones y borrar datos.
Si un programa lo interpretara como una orden, podría borrar los comentarios
sin autorización. registry.py lo devuelve dentro de untrusted_data; la lista
ACTIONS admite solo acciones conocidas y _valid_args comprueba nombres y tipos.
No hay eval ni SQL libre. Incluso si el modelo pide borrar, solo recibe un plan.

La prueba de borrado se limitó a los datos de práctica del artículo 5 y después
se restauró con seed_blog. Los registros 17 a 20 muestran el plan, la ejecución
con --approve y cero comentarios tras el borrado.

Después se pidió otro plan, se agregó un comentario y se reutilizó el hash viejo.
El resultado fue approval_required: el plan actual tiene otros IDs y otro hash.
Los dos comentarios quedaron presentes. Los registros 21 a 25 muestran este
caso y la restauración final a 4 autores, 15 artículos y 23 comentarios.

Se fijan IDs de artículos 1 a 15 en seed_blog para que repetir la carga mantenga
válidos los ejemplos --post_id 1 y 5. Los otros modelos no requieren IDs fijos.
Los hash provienen de los comandos ejecutados; no se inventan ni se reutilizan
como credenciales. Esta demostración se hace con autorización de la práctica;
una operación real requeriría revisar y aprobar su plan específico.

Este registro didáctico no demuestra protección frente a cambios concurrentes
entre la comprobación del hash y el borrado. El ejemplo del docente comprueba
el cambio antes de aprobar; no se amplía su alcance sin evidencia.
