#3
"""path: Se utiliza para definir rutas o URLs en Django.
include: Permite incluir otras URLs o rutas de diferentes aplicaciones en el proyecto."""
from django.urls import path, include

from rest_framework.documentation import include_docs_urls


"""routers: De Django REST Framework, se utiliza para crear un conjunto de rutas automáticas basadas en el modelo que registras."""
from rest_framework import routers
"""views: Importa las vistas desde la aplicación tasks, donde se define la lógica de la API."""
from tasks import views


"""router = routers.DefaultRouter(): Se crea una instancia del enrutador por defecto de DRF. Este enrutador genera automáticamente las rutas estándar para realizar las operaciones CRUD (Create, Read, Update, Delete)."""
router = routers.DefaultRouter()
"""r'tasks': Es el prefijo de la URL. Todas las URLs relacionadas con las tareas (tasks) comenzarán con este prefijo.
views.TaskView: Es la vista que maneja las solicitudes relacionadas con el modelo Task. Esta vista hereda de ModelViewSet, por lo que tiene las operaciones CRUD integradas.
'tasks': Es el nombre del conjunto de rutas."""
"""Esto genera automáticamente rutas como:
GET /api/v1/tasks/ (Listar todas las tareas)
POST /api/v1/tasks/ (Crear una nueva tarea)
GET /api/v1/tasks/<id>/ (Obtener detalles de una tarea específica)
PUT /api/v1/tasks/<id>/ (Actualizar una tarea específica)
DELETE /api/v1/tasks/<id>/ (Eliminar una tarea específica)"""
router.register(r'tasks', views.TaskView, 'tasks')

"""urlpatterns: Es una lista que contiene todas las rutas de tu aplicación.
path("api/v1/", include(router.urls)): Define que todas las URLs que empiecen con api/v1/ serán gestionadas por el enrutador que definiste anteriormente.
Por ejemplo, para acceder a las rutas de las tareas, la URL sería: http://localhost:8000/api/v1/tasks/"""
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Tasks API"))
]


"""Este código crea una API RESTful para manejar las tareas (tasks), donde se pueden realizar operaciones CRUD usando un ViewSet y las rutas generadas automáticamente por el DefaultRouter de Django REST Framework.
El prefijo api/v1/ indica que esta es la versión 1 de tu API. Es común versionar las APIs para poder hacer cambios futuros sin romper versiones anteriores.
"""
