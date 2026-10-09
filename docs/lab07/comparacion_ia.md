# Comparación y uso de IA

## Puntos 6 y 7 Comparación con las respuestas del docente

| Pregunta | Respuesta implementada | IA del docente | Decisión y evidencia |
|---|---|---|---|
| q1 | Publicados, 1 consulta | Correcta, 1 consulta | Aceptar. Coincide con el oráculo. |
| q2 | Sin categoría, 1 consulta | Correcta, 1 consulta | Aceptar. Usa isnull. |
| q3 | Fechas inclusivas, 1 consulta | Resultado distinto | Rechazar. gt y lt excluyen 1 de marzo y 31 de mayo; range incluye ambos. |
| q4 | Count y filtro en BD, 1 consulta | Correcta pero cara, 16 consultas | Rechazar como solución final. Consulta 15 conteos y filtra en Python. |
| q5 | Dos conteos distintos, 1 consulta | Conteos multiplicados | Rechazar. Los JOIN de comentarios y etiquetas multiplican filas; usar distinct en ambos Count. |
| q6 | author__profile__country, 1 consulta | FieldError | Rechazar. country pertenece a Profile, no a Author. |
| q7 | post__category__name, 1 consulta | Correcta, 1 consulta | Aceptar. Atraviesa ambas relaciones. |
| q8 | Excluir autores con publicaciones, 1 consulta | Resultado distinto | Rechazar. Tener borradores no significa nunca publicar; también omite a Diego, que no tiene artículos. |

Los mensajes reales y el SQL generado por Django están en resultados/08 y 09.
Mostrar el SQL para explicar una consulta no implica escribir ni ejecutar SQL crudo.

## Punto 8 Nueva propuesta de un asistente

Se registró una segunda propuesta de Codex en codex_answers.py, usando los
modelos revisados. Se ejecutó con run_all, el mismo verificador del duelo,
mediante manage.py shell (resultado 10_duelo_codex.txt): ocho correctas y
una consulta por pregunta. q3 usa gte/lte y q8 usa Exists.
Codex tenía el contexto de esta conversación y había visto los fallos del
docente; esta comparación no representa un experimento ciego ni un segundo
modelo independiente. No se inventaron fallos para completar la tabla.

## Uso de IA durante la práctica

Se autorizó a Codex a implementar las consultas, ejecutar las pruebas y documentar
los resultados. Por ello, las funciones de team.py fueron elaboradas con ayuda
de IA: no se presentan como respuestas escritas sin asistencia por la alumna.
Las ocho pasaron en el primer intento registrado. La alumna debe revisar y
explicar las relaciones, los conteos y los filtros para demostrar su aprendizaje.
Se aceptaron las propuestas después de comprobarlas contra el oráculo del docente.
Las respuestas defectuosas del módulo ai_answers.py permanecen sin corregir para
que la comparación sea reproducible.
