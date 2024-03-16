import keyboard
from random import randint
import setup
import objects
from sys import exit


class Cell:
    '''
    Клетка игрового поля

    Attributes
    ----------
        y : int
            координата y - индекс ряда клеток на поле
        x : int
            координата x - индекс клетки в ряду поля
        content : None | Player | Obstacle
            контент клетки
        image: str
            символ, отображающий контент клетки на поле
    '''

    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.content = None
        self.image = setup.CELL_IMAGE

    def draw(self):
        if self.content:
            print(self.content.image, end=' ')
        else:
            print(self.image, end=' ')


class Field:
    def __init__(self) -> None:
        self.rows = 10
        self.columns = 3
        self.player = objects.Player(y=self.rows - 1,
                                     x=self.columns // 2)
        self.obstacles = []
        self.field = self.generate_empty_field()
        self.field[self.player.y][self.player.x].content = self.player 

    def spawn_obstacle(self) -> None:
        obstacle_y, obstacle_x = 0, randint(0, 2)
        if self.check_neighbours(obstacle_y, obstacle_x):
            obstacle = objects.Obstacle(obstacle_y, obstacle_x)
            self.obstacles.append(obstacle)
            self.field[obstacle.y][obstacle.x].content = obstacle

    def check_neighbours(self, y, x) -> bool:
        if not self.field[y + 1][x].content and not self.field[y + 2][x].content:
                return True
    
    def move_obstacles(self) -> None:
        for obstacle in self.obstacles:
            this_cell = self.field[obstacle.y][obstacle.x]
            if not self.is_on_field(obstacle.y + 1,
                                    obstacle.x):
                this_cell.content = None
                self.obstacles.remove(obstacle)
                continue
            obstacle.y += 1
            new_cell = self.field[obstacle.y][obstacle.x]
            this_cell.content = None
            new_cell.content = obstacle


    def generate_empty_field(self) -> list[list[Cell]]:
        '''Создает пустое поле'''
        field = [
            [Cell(y=row, x=column) for column in range(self.columns)]
            for row in range(self.rows)
        ]
        return field
    
    def is_on_field(self, y: int, x: int) -> bool:
        '''Возвращает True, если клетка[y][x] в пределах поля'''
        return (y > -1 and y < self.rows) and (x > -1 and x < self.columns) 
    
    def move_player(self) -> bool:
        '''
        Перемещает игрока по полосам движения при нажатии клавиш движения
        Проверяет коллизии с границами поля
        Проверяет коллизии с препятствиями
        При удачном перемещении возвращает True
        При неудачном перемещении(столкновение с границей поля или препятствием) возвращает False
        '''
        dx = 0
        if keyboard.is_pressed(setup.KEYS['right']):
            dx = 1
        if keyboard.is_pressed(setup.KEYS['left']):
            dx = -1
        if keyboard.is_pressed(setup.KEYS['exit']):
            exit()

        this_cell = self.field[self.player.y][self.player.x]
        new_x = self.player.x + dx

        # коллизия с границей поля
        if not self.is_on_field(self.player.y, new_x):
            return False

        new_cell = self.field[self.player.y][new_x]

        # Коллизия с препятствием
        if isinstance(new_cell.content, objects.Obstacle):
            return False
        
        # Успешное перемещение
        this_cell.content = None
        new_cell.content = self.player
        self.player.x = new_x
        return True
    
    def draw(self) -> None:
        '''
        Рисует поле и его границы
        '''
        for row in self.field:
            print(setup.WALL + ' ', end='')
            for cell in row:
                cell.draw()
            print(setup.WALL)
        print('')