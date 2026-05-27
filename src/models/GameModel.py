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
    def comprar_juego(self, id_cliente, id_juego, id_consola):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO ventas(id_cliente, id_juego, id_consola, fecha)
        VALUES(%s, %s, %s, CURDATE())
        """
        cursor.execute(query, (id_cliente, id_juego, id_consola))
        conn.commit()
        conn.close()


    def obtener_compras(self, id_cliente):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT ventas.id_venta,
               juegos.nombre AS juego,
               consolas.nombre_consola AS consola,
               ventas.fecha
        FROM ventas
        INNER JOIN juegos
        ON ventas.id_juego = juegos.id_juego
        INNER JOIN consolas
        ON ventas.id_consola = consolas.id_consola
        WHERE ventas.id_cliente = %s
        """
        cursor.execute(query, (id_cliente,))
        compras = cursor.fetchall()
        conn.close()
        return compras

    def eliminar_compra(self, id_venta):

        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM ventas WHERE id_venta = %s"
        cursor.execute(query, (id_venta,))
        conn.commit()
        conn.close()

