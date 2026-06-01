from models.databaseModel import Database


class GameModel:

    def __init__(self):
        self.db = Database()

    def obtener_juegos(self):
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

        conn = self.db.get_connection()

        try:
            cursor = conn.cursor()

            query = """
                INSERT INTO ventas(
                    id_cliente,
                    id_juego,
                    id_consola,
                    fecha,
                    estado
                )
                VALUES(
                    %s,
                    %s,
                    %s,
                    CURDATE(),
                    'Pendiente'
                )
            """

            cursor.execute(
                query,
                (
                    id_cliente,
                    id_juego,
                    id_consola
                )
            )

            conn.commit()

        finally:
            cursor.close()
            conn.close()

    def obtener_compras(self, id_cliente):

        conn = self.db.get_connection()

        try:
            cursor = conn.cursor(dictionary=True)

            query = """
                SELECT ventas.id_venta,
                   juegos.nombre AS juego,
                   consolas.nombre_consola AS consola,
                   ventas.fecha,
                   ventas.estado
                FROM ventas
                INNER JOIN juegos
                ON ventas.id_juego = juegos.id_juego
                INNER JOIN consolas
                ON ventas.id_consola = consolas.id_consola
                WHERE ventas.id_cliente = %s
        """

            cursor.execute(
            query,
            (id_cliente,)
            )

            compras = cursor.fetchall()

            return compras

        finally:
            cursor.close()
            conn.close()

    def cambiar_estado(self, id_venta):

        conn = self.db.get_connection()

        try:
            cursor = conn.cursor()

            query = """
                UPDATE ventas
                SET estado =
                    CASE
                        WHEN estado = 'Pendiente'
                        THEN 'Entregado'
                        ELSE 'Pendiente'
                    END
                WHERE id_venta = %s
            """

            cursor.execute(
                query,
                (id_venta,)
            )

            conn.commit()

        finally:
            cursor.close()
            conn.close()

    def eliminar_compra(self, id_venta):

        conn = self.db.get_connection()

        try:
            cursor = conn.cursor()

            query = """
                DELETE FROM ventas
                WHERE id_venta = %s
            """

            cursor.execute(
                query,
                (id_venta,)
            )

            conn.commit()

        finally:
            cursor.close()
            conn.close()