from models.GameModel import GameModel

class GameController:

    def __init__(self):
        self.model = GameModel()

    def obtener_juegos(self):
        return self.model.obtener_juegos()

    def comprar_juego(self, id_cliente, id_juego, id_consola):
        self.model.comprar_juego(id_cliente, id_juego, id_consola)

    def obtener_compras(self, id_cliente):
        return self.model.obtener_compras(id_cliente)

    def eliminar_compra(self, id_venta):
        self.model.eliminar_compra(id_venta)
