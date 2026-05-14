from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuarioBaseShema(BaseModel):
    nombre: str= Field(min_length=3, max_length=100)
    apellido: Optional[str] = None
    email: EmailStr
    password: str= Field(min_length=8)
    telefono: Optional[str] = None
    fecha: Optional[str] = None
    
class UsuarioShema(UsuarioBaseShema):
    email: EmailStr
    password: str= Field(min_length=8)

