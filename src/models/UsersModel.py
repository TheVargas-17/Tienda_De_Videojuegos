import bcrypt
from models.databaseModel import Database


class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # verificar duplicado por correo
            cursor.execute(
                "SELECT * FROM clientes WHERE correo=%s",
                (usuario.correo,)
            )
            if cursor.fetchone():
                return False

            # encriptar contraseña
            hashed = bcrypt.hashpw(
                usuario.contrasena.encode('utf-8'),
                bcrypt.gensalt()
            )

            # insertar en clientes
            cursor.execute(
                """
                INSERT INTO clientes (nombre, telefono, correo, contrasena)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    usuario.nombre,
                    usuario.telefono,
                    usuario.correo,
                    hashed.decode('utf-8')
                )
            )

            conn.commit()
            return True

        except Exception as e:
            print("ERROR REGISTRO:", e)
            return False

        finally:
            conn.close()

    def validar_login(self, correo, contrasena):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT * FROM clientes WHERE correo=%s",
                (correo,)
            )
            user = cursor.fetchone()

            if not user:
                return None

            if bcrypt.checkpw(
                contrasena.encode('utf-8'),
                user['contrasena'].encode('utf-8')
            ):
                return user

            return None

        except Exception as e:
            print("ERROR LOGIN:", e)
            return None

        finally:
            conn.close()