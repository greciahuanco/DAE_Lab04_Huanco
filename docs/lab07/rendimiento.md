# Puntos 9 a 11 Consultas N+1

La prueba inicial falló: 23 consultas ejecutadas frente a 2 esperadas.
El registro 11_prueba_roja.txt incluye el mensaje y el SQL capturado por Django.
Hay 11 artículos publicados: 1 consulta de artículos, 11 consultas al acceder
al autor y 11 consultas al acceder a las etiquetas. Total: 1 + 11 + 11 = 23.
Sin optimización el costo crece como 1 + 2N.

select_related("author") trae cada autor con el artículo mediante JOIN:
corresponde a la relación ForeignKey. prefetch_related("tags") usa otra consulta
para reunir las etiquetas de todos los artículos: corresponde a ManyToManyField.
Después, el mismo assertNumQueries(2) pasa; esta prueba no se modifica.

La suite inicial (registro 13) también esperaba que team.py estuviera vacío.
Una vez resueltas las consultas, esa expectativa ya no describe el proyecto.
Se reemplaza por una comprobación de las ocho respuestas correctas y una consulta
por respuesta, conservando el oráculo y los límites del docente. La suite final
(registro 14) ejecuta 24 pruebas sin fallos; dos se omiten porque la carpeta
privada teacher/ con las soluciones de referencia no fue distribuida.
