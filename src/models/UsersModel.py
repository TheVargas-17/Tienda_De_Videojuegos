import bcrypt
from models.databaseModel import Database


class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # verificar duplicado
            cursor.execute(
                "SELECT * FROM usuario WHERE correo=%s",
                (usuario.correo,)
            )
            if cursor.fetchone():
                return False

            hashed = bcrypt.hashpw(
                usuario.contrasena.encode('utf-8'),
                bcrypt.gensalt()
            )

            cursor.execute(
                """
                INSERT INTO usuario (nombre, apellidos, edad, correo, contrasena)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    usuario.nombre,
                    usuario.apellidos,
                    usuario.edad,
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
                "SELECT * FROM usuario WHERE correo=%s",
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