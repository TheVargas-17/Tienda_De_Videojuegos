from models.GameModel import GameModel

class GameController:

    def __init__(self):
        self.model = GameModel()

    def obtener_juegos(self):
        return self.model.obtener_juegos()

