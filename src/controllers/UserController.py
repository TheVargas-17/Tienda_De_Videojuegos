from models.UsersModel import UsuarioModel
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError


class AuthController:

    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, apellidos, edad, correo, contrasena):
        try:
            nuevo = UsuarioSchema(
                nombre=nombre,
                apellidos=apellidos,
                edad=edad,
                correo=correo,
                contrasena=contrasena
            )

            success = self.model.registrar(nuevo)

            if success:
                return True, "Usuario creado correctamente"
            return False, "El usuario ya existe"

        except ValidationError as e:
            return False, e.errors()[0]['msg']

        except Exception as e:
            print("ERROR REGISTRO:", e)
            return False, "Error interno"

    def login(self, correo, contrasena):
        try:
            user = self.model.validar_login(correo, contrasena)

            if user:
                return user, "Login correcto"
            return None, "Credenciales incorrectas"

        except Exception as e:
            print("ERROR LOGIN:", e)
            return None, "Error interno"