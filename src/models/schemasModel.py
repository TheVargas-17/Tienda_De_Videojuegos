from pydantic import BaseModel, EmailStr, Field


class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    apellidos: str = Field(min_length=2, max_length=150)
    edad: int = Field(ge=0, le=120)
    correo: EmailStr
    contrasena: str = Field(min_length=8)