#1
"""
Un serializador en Django REST Framework toma los datos de un modelo o cualquier 
tipo de entrada y los convierte en un formato que pueda ser fácilmente transferido 
a través de una API (como JSON o XML). De la misma manera, los datos entrantes en 
la API pueden ser deserializados para ser procesados y guardados en el modelo.
Este serializador puede ser usado en vistas basadas en API, como en views.py, 
para convertir las instancias del modelo Task en formato JSON (o el formato necesario) 
cuando se hace una solicitud HTTP.
"""
from rest_framework import serializers
from .models import Task

"""es una clase de atajo que automatiza la creación de serializadores 
basados en modelos. Se basa en la estructura del modelo para definir 
los campos y la validación de los datos, reduciendo la necesidad de 
definir manualmente los campos de un serializador."""
class TaskSerializar(serializers.ModelSerializer):
    """es una convención en Django que se usa para definir 
    metadatos sobre la clase TaskSerializer, como qué modelo 
    se está serializando y qué campos incluir."""
    class Meta:
        """Informa al serializador que los campos y la estructura 
        de datos deben coincidir con los del modelo Task"""
        model = Task
        """ignifica que se van a serializar todos los campos 
        definidos en el modelo Task (por ejemplo, id, title, description, y done). 
        Como alternativa, podrías listar campos específicos 
        si solo quisieras incluir algunos de ellos."""
        # fields = ('id', 'title', 'description', 'done')
        fields = '__all__'