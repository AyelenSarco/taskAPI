# taskAPI
Este proyecto es una API de tareas desarrollada con Python, FastAPI, SQLAlchemy y Alembic. Cada usuario puede registrarse, autenticarse mediante tokens JWT, y gestionar sus tareas de manera segura, con una logica de acceso que garantiza que los usuarios solo puedan interactuar con sus propias tareas.

## Tecnologias usadas

- Python: Lenguaje principal utilizado para desarrollar la API.
- FastAPI: Framework para la construcción rápida y sencilla de APIs, ofreciendo alto rendimiento.
- SQLAlchemy: ORM utilizado para interactuar con la base de datos SQLite, permitiendo el mapeo de objetos de Python a tablas de bases de datos.
- SQLite: Base de datos ligera, utilizada para almacenar y gestionar las tareas de los usuarios.
- OAuth2: Implementado para la autenticación y autorización segura en la API.
- JWT Tokens: Utilizados para la autenticación de usuarios a través de tokens seguros.
- Pipenv: Herramienta de gestión de entornos y dependencias, que facilita el manejo de paquetes y entornos virtuales.

## Instalación:
- Cola el repositorio: git clone https://github.com/AyelenSarco/taskAPI.git
- Navega al directorio del proyecto : cd taskAPI
- Instala las dependencias usando Pipenv: pipenv install
- Activa el entorno virtual: pipenv shell

## Uso
- Para iniciar la api usa: uvicorn app.main:app --reload
- Visita http://127.0.0.1:8000/docs para ver la documentación interactiva generada automáticamente por FastAPI.
