# Despliegue de la API

## La API FastAPI indica que se cree un entorno virtual para que su uso sea correcto

### 1. Creación del entorno virtual

Para crear un entorno virtual, decide en que carpeta quieres crearlo y ejecuta el módulo venv como script con la ruta a la carpeta:


py
python -m venv tutorial-env

Esto creará el directorio tutorial-env si no existe, y también creará directorios dentro de él que contienen una copia del intérprete de Python y varios archivos de soporte.

Una ruta común para el directorio de un entorno virtual es .venv. Ese nombre mantiene el directorio típicamente escondido en la consola y fuera de vista mientras le da un nombre que explica cuál es el motivo de su existencia. También permite que no haya conflicto con los ficheros de definición de variables de entorno .env que algunas herramientas soportan.

