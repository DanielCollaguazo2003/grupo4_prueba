from pydantic import BaseModel
from datetime import date

class Cliente(BaseModel):
    nombre: str
    email: str
    telefono: str

class Habitacion(BaseModel):
    numero: int
    tipo: str
    estado: bool
    precio_por_noche: float
    precio_por_dia: float

class Servicio(BaseModel):
    descripcion: str
    precio: float

class Reserva(BaseModel):
    id_cliente: int
    fecha_reserva: date
    duracion_estancia: int
    estado_reserva: str
    monto_total: float
