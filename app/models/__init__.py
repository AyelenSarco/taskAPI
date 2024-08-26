# Importa y define todos los modelos aquí
from .task_model import Task
from .user_model import User

# Esto asegura que todos los modelos se registren en la metadata
__all__ = ["Task", "User"]