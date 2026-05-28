from models.databaseModel import Database


class GameModel:

    def __init__(self):
        self.db = Database()

    def obtener_juegos(self):
        """Obtiene todos los juegos con la consola y la imagen"""
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT juegos.*, consolas.nombre_consola
                FROM juegos
                INNER JOIN consolas
                ON juegos.id_consola = consolas.id_consola
            """
            cursor.execute(query)
            juegos = cursor.fetchall()
            return juegos
        finally:
            cursor.close()
            conn.close()

    def comprar_juego(self, id_cliente, id_juego, id_consola):
        """Inserta una venta en la base de datos"""
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO ventas(id_cliente, id_juego, id_consola, fecha)
                VALUES(%s, %s, %s, CURDATE())
            """
            cursor.execute(query, (id_cliente, id_juego, id_consola))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def obtener_compras(self, id_cliente):
        """Obtiene todas las compras de un cliente"""
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT ventas.id_venta,
                       juegos.nombre AS juego,
                       juegos.imagen AS imagen,
                       consolas.nombre_consola AS consola,
                       ventas.fecha
                FROM ventas
                INNER JOIN juegos ON ventas.id_juego = juegos.id_juego
                INNER JOIN consolas ON ventas.id_consola = consolas.id_consola
                WHERE ventas.id_cliente = %s
            """
            cursor.execute(query, (id_cliente,))
            compras = cursor.fetchall()
            return compras
        finally:
            cursor.close()
            conn.close()

    def actualizar_fecha(self, id_venta):
        """Actualiza la fecha de una venta a la fecha actual"""
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            query = """
                UPDATE ventas
                SET fecha = CURDATE()
                WHERE id_venta = %s
            """
            cursor.execute(query, (id_venta,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def eliminar_compra(self, id_venta):
        """Elimina una venta por su id"""
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            query = """
                DELETE FROM ventas
                WHERE id_venta = %s
            """
            cursor.execute(query, (id_venta,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()