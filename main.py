from os import system, name
import assets
import keyboard
from field import Field
import setup
from time import sleep


class Application:
    '''
    Основная программа

    Attributes
    ----------
        is_running : bool
            контролирует главный цикл программы
        game : Game
            экземпляр игровой сессии
    '''
    def __init__(self) -> None:
        self.is_running = True
        self.game = Game()
        self.run()

    def run(self) -> None:
        '''
        Показывает стартовый экран с картинкой и историей,
        запускает новую игру,
        показывает меню в конце игры
        '''
        self.show_start_screen()
        while self.is_running:
            self.game.start_new_game()
            self.show_end_screen()

    def show_start_screen(self) -> None:
        ''' Выводит на экран ASCII картинку и текст истории '''
        self.clear_screen()
        print(assets.logo)
        print(assets.story)
        input('Нажмите ENTER чтобы начать игру')

    def show_end_screen(self) -> None:
        ''' Выводит на экран меню выбора: новая игра и выход '''
        print('Enter - сыграть еще раз')
        print('Esc - выход')

        while True:
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'esc':
                    self.is_running = False
                    return
                elif event.name == 'enter':
                    return
    
    def clear_screen(self) -> None:
        if name == 'nt':
            system('cls')
        else:
            system('clear')

class Game:
    def __init__(self) -> None:
        pass
    
    def start_new_game(self) -> None:
        '''Запускает новую игровую сессию'''
        self.field = Field()
        self.is_running = True
        self.run()
    
    def show_score(self) -> None:
        print(f'Очков: {self.field.player.score}')
    
    def run(self) -> None:
        '''
        Главный цикл игры:
            очищает экран
            отрисовывает поле
        '''
        while self.is_running:
            if name == 'nt':
                system('cls')
            else:
                system('clear')
            
            self.field.draw()

            move = self.field.move_player()
            self.field.spawn_obstacle()
            self.field.move_obstacles()
            self.show_score() 
            if not move:
                self.is_running = False
            self.field.player.score += 100
            sleep(1 / setup.FPS)
        # конец игры
        
        system('cls')
        self.field.draw()
        print(
            setup.LIGHT_PURPLE
            + 'Конец игры!'
            + setup.END_COLOR
        )


if __name__ == '__main__':
    Application()
