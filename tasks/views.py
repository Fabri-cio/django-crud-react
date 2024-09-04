#2
"""Los viewsets en DRF son una manera de agrupar las vistas comunes para las operaciones CRUD en un solo lugar. Esto hace que el código sea más sencillo y fácil de mantener, ya que no es necesario escribir manualmente las vistas para cada operación."""
from rest_framework import viewsets
"""El TaskSerializar se usa para convertir las instancias del modelo Task a JSON (u otro formato) cuando se responde a una solicitud HTTP, y para deserializar los datos cuando se crean o actualizan tareas a través de la API."""
from .serializer import TaskSerializar
"""El modelo Task define la estructura de los datos en la base de datos, y es la fuente de los datos que la API expone."""
from .models import Task

# Create your views here.
"""Define una clase llamada TaskView, que hereda de viewsets.ModelViewSet.
ModelViewSet es una clase de vista en DRF que proporciona automáticamente todas las acciones estándar para un modelo, como list (listar), create (crear), retrieve (recuperar una instancia), update (actualizar), y delete (eliminar). Esta clase permite exponer todas estas funcionalidades para el modelo Task en una API RESTful, sin necesidad de escribir mucho código adicional.
"""
class TaskView(viewsets.ModelViewSet):
    """El serializador TaskSerializar se utiliza para definir cómo los datos del modelo Task deben ser convertidos a JSON u otro formato, y cómo se deben interpretar los datos entrantes (por ejemplo, al crear o actualizar una tarea)."""
    serializer_class = TaskSerializar
    """Task.objects.all() devuelve todas las instancias del modelo Task de la base de datos. Este es el conjunto de datos que será expuesto a través de la API. La vista proporcionará acceso a todas las tareas almacenadas en la base de datos, permitiendo que se puedan listar, crear, actualizar o eliminar."""
    queryset = Task.objects.all()

    """
    ViewSet: Es una clase en Django REST Framework que agrupa las acciones CRUD comunes (como create, retrieve, update, delete) en un solo lugar. En lugar de definir vistas individuales para cada operación, como listar, crear, actualizar y eliminar, el ViewSet lo hace todo automáticamente.
    ModelViewSet: Es un tipo de ViewSet que maneja automáticamente todas las acciones basadas en un modelo (como Task), como listar, crear, recuperar, actualizar y eliminar.
    """