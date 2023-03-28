from function import *

# главный цикл программы
while not is_game_close():
    event()
    simulation()
    display()

# выход из игры
quit_game()