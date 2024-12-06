from pydantic import BaseModel

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
