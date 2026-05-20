
from utils.email_sender import enviar_correo
from models.UsersModel import UsuarioModel
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:

    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, telefono, correo, contrasena):

        try:

            nuevo = UsuarioSchema(
                nombre=nombre,
                telefono=telefono,
                correo=correo,
                contrasena=contrasena
            )

            success = self.model.registrar(nuevo)

            if success:
                return True, "Usuario creado correctamente"

            return False, "El usuario ya existe"

        except ValidationError as e:

            return False, e.errors()[0]["msg"]

        except Exception as e:

            print("ERROR REGISTRO:", e)

            return False, "Error interno"

    def login(self, correo, contrasena):

        try:

            user = self.model.validar_login(
                correo,
                contrasena
            )

            if user:
                return user, "Login correcto"

            return None, "Credenciales incorrectas"

        except Exception as e:

            print("ERROR LOGIN:", e)

            return None, "Error interno"

    def recuperar_contrasena(self, correo, nueva_contrasena):

        try:

            success = self.model.actualizar_contrasena(
                correo,
                nueva_contrasena
            )

            if not success:

                return False, "Correo no encontrado"

            enviado = enviar_correo(
                correo,
                "Contraseña actualizada",
                "Tu contraseña fue cambiada correctamente."
            )

            if enviado:

                return True, "Contraseña actualizada"

            return False, "No se pudo enviar el correo"

        except Exception as e:

            print("ERROR RECUPERAR:", e)

            return False, "Error interno"