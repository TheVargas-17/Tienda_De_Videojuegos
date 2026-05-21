from models.databaseModel import Database

class GameModel:

    def __init__(self):
        self.db = Database()

    def obtener_juegos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT juegos.*, consolas.nombre_consola
        FROM juegos
        INNER JOIN consolas
        ON juegos.id_consola = consolas.id_consola
        """
        cursor.execute(query)
        juegos = cursor.fetchall()
        conn.close()
        return juegos
