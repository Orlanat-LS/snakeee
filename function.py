from data import *

def is_game_close(): # проверить надобность выхода из программы
    return game_close


def event(): # Обработать события
    global game_close
    for event in pygame.event.get():
        print(event)  # выводит на экран все действия игры
        if event.type == pygame.QUIT:  # нажатие на выход
            game_close = True

def simulation(): # Выполнить логику программы
    pass
def display(): # Отрисовать все объекты
    pygame.draw.rect(dis, (255, 255, 255), (75, 75, 50, 50))
    pygame.display.update()
def quit_game(): # Выйти из программы
    quit()