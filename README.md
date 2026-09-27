# DAE - Laboratorio 05

## Administrador de Django

En este laboratorio se continuó trabajando sobre el proyecto del Laboratorio 04 y se utilizó el administrador de Django para gestionar un nuevo módulo de películas.

## Modelos

Se creó la aplicación `movies` con los siguientes modelos:

- Genre
- Person
- Movie
- Rating

Estos modelos permiten registrar géneros, personas relacionadas como directores, películas y sus respectivas valoraciones.

## Funcionalidades realizadas

- Creación y registro de los modelos de películas en Django Admin.
- Personalización del administrador de películas.
- Uso de `list_display` para mostrar información relevante.
- Implementación de filtros por año y género.
- Implementación de búsqueda de películas.
- Uso de `RatingInline` para administrar valoraciones desde una película.
- Configuración de campos de auditoría como solo lectura.
- Registro de datos de prueba desde Django Admin.
- Creación del grupo `editores`.
- Configuración de permisos para agregar y modificar películas sin permitir su eliminación.
- Creación de un usuario perteneciente al grupo `editores`.
- Comprobación de las diferencias entre el acceso del superusuario y el usuario editor.
- Implementación de una vista pública de recomendaciones.
- Recomendación de películas del mismo género ordenadas según su valoración promedio.

## Vista de recomendaciones

Se implementó una vista pública que permite seleccionar una película y obtener recomendaciones de otras películas que pertenecen al mismo género.

Las recomendaciones utilizan el promedio de las valoraciones registradas y se ordenan de mayor a menor valoración.
