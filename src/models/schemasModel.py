from pydantic import BaseModel, EmailStr, Field


class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    telefono: str = Field(min_length=10, max_length=15)
    correo: EmailStr
    contrasena: str = Field(min_length=8)