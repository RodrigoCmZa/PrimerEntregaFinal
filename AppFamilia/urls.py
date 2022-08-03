from django.urls import path

from AppFamilia.views import (
    Inicio,
    busqueda_familiar,
    buscar_persona,
    crear_tareas,
    editar_tareas,
    eliminar_tarea,
    mostrar_tarea,
    crear_persona,
    mostrar_familia,
    editar_persona,
    eliminar_persona,
    crear_herramienta,
    mostrar_herramientas,
    editar_herramienta,
    eliminar_herramienta
)

# Codigo de Vitor Lira , PrimerMVT - Coder.

urlpatterns = [
    path("", Inicio),
    path("tarea/", mostrar_tarea, name='mostrar_tareas'),
    path("tarea/crear", crear_tareas, name='crear_tareas'),
    path("tarea/editar/<id>", editar_tareas, name='editar_tareas'),
    path("tarea/eliminar/<id>", eliminar_tarea, name='eliminar_tarea'),
    path("crear/persona", crear_persona, name="crear_persona"),
    path("familia/", mostrar_familia, name="mostrar_familia"),
    path("persona/editar/<id>", editar_persona, name='editar_persona'),
    path("persona/eliminar/<id>", eliminar_persona, name='eliminar_persona'),
    path("buscar_familiar/", busqueda_familiar, name='busqueda_familiar'),
    path("buscar/", buscar_persona, name='buscar_persona'),
    path("crear/herramienta",crear_herramienta ,name='crear_herramientas'),
    path("mostrar/herramientas",mostrar_herramientas ,name='mostrar_herramientas'),
    path("editar/herramienta/<id>",editar_herramienta,name='editar_herramienta'),
    path("eliminar/herramienta/<id>",eliminar_herramienta,name='eliminar_herramienta')
    
]
