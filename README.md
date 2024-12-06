# API de Reserva de Hotel - FastAPI

Este proyecto implementa una API REST para gestionar un sistema de reservas de hotel. Permite administrar **clientes**, **habitaciones**, **servicios** y **reservas** de manera eficiente. La API está construida con **FastAPI** y sigue principios de arquitectura limpia.

## Integrantes del Proyecto

- **Collaguazo Malla Daniel Alfredo**
- **Delgado Ibujes Domenika Sofia**
- **Pañora Uruchima Jeison Fabian**
- **Sigua Calle Paúl Mateo**
- **Villalta Heredia José Miguel**

## 1. Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- Git
- FastAPI
- Uvicorn
  
## 2. Configuración del Entorno Virtual

Se recomienda usar un entorno virtual para aislar las dependencias:

### En Windows:
```bash
python -m venv env
env\Scripts\activate
```
### En Unix o MacOS:
```bash
python3 -m venv env
source env/bin/activate
```

## 3. Instalación de Dependencias

Con el entorno virtual activado, instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

Si el archivo `requirements.txt` no existe, instala FastAPI y Uvicorn manualmente:

```bash
pip install fastapi uvicorn
```

## 4. Ejecución de la API

Para iniciar el servidor de desarrollo:

```bash
uvicorn app:app --reload
```

- **app:app**: El primer `app` es el nombre del archivo y el segundo es la instancia de FastAPI.
- **--reload**: Recarga automáticamente el servidor al detectar cambios.

La API estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 5. Documentación Interactiva

FastAPI ofrece una documentación interactiva generada automáticamente:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

## 6. Endpoints Principales

### Clientes

- **POST** `/clientes`: Agrega un nuevo cliente.

### Servicios

- **POST** `/servicios`: Agrega un nuevo servicio.

### Habitaciones

- **POST** `/habitaciones`: Agrega una nueva habitación.

*(Agrega más detalles si es necesario)*

## 7. Desactivación del Entorno Virtual

Una vez terminado, puedes desactivar el entorno virtual con:

```bash
deactivate
```
