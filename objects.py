import setup


class GameObject:
    '''
    Объект на игровом поле
    '''

    def __init__(self, y, x, image):
        self.y = y
        self.x = x
        self.image = image


class Player(GameObject):
    def __init__(self, y, x, image=setup.PLAYER_IMAGE):
        self.score = 0
        super().__init__(y, x, image)


class Obstacle(GameObject):
    def __init__(self, y, x, image=setup.OBSTACLE_IMAGE):
        super().__init__(y, x, image)