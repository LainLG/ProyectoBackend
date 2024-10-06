from typing import Optional
from pydantic import BaseModel


class CrearProducto(BaseModel):
    nombre: str
    tipo: Optional[str] = None
    valorunitario: float
    valorventa: float
    cantidadtotal: Optional[int] = None


class ActualizarProducto(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    valorunitario: Optional[float] = None
    valorventa: Optional[float] = None
    cantidadtotal: Optional[int] = None


