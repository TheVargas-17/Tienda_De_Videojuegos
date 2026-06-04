import random

from utils.email_sender import enviar_correo
from models.UsersModel import UsuarioModel
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError


class AuthController:

    def __init__(self):
        self.model = UsuarioModel()
        self.codigos_recuperacion = {}

    # ===== REGISTRO =====

    def registrar_usuario(
        self,
        nombre,
        telefono,
        correo,
        contrasena
    ):

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

    # ===== LOGIN =====

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

    # ===== ENVIAR CODIGO =====

    def enviar_codigo_recuperacion(self, correo):

        try:

            codigo = str(random.randint(100000, 999999))

            enviado = enviar_correo(
                correo,
                "Recuperación de contraseña",
                f"Tu código de recuperación es: {codigo}"
            )

            if not enviado:
                return False, "No se pudo enviar el correo"

            self.codigos_recuperacion[correo] = codigo

            return True, "Código enviado correctamente"

        except Exception as e:

            print("ERROR ENVIAR CODIGO:", e)

            return False, "Error interno"

    # ===== RECUPERAR CONTRASEÑA =====

    def recuperar_contrasena(
        self,
        correo,
        codigo,
        nueva_contrasena
    ):

        try:

            codigo_guardado = self.codigos_recuperacion.get(correo)

            if not codigo_guardado:
                return False, "Primero solicita un código"

            if codigo != codigo_guardado:
                return False, "Código incorrecto"

            success = self.model.actualizar_contrasena(
                correo,
                nueva_contrasena
            )

            if not success:
                return False, "Correo no encontrado"

            del self.codigos_recuperacion[correo]

            return True, "Contraseña actualizada"

        except Exception as e:

            print("ERROR RECUPERAR:", e)

            return False, "Error interno"