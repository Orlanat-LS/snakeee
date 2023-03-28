import pygame

# инициализация экрана
pygame.init()


# параметры игры
rect_size = 20 # размер кубика на сетке (в пикселях)
field_size = 20 # размер игрового поля в ширину и в высоту (в кубиках)
screen_size = ( # размер экрана (в пикселях)
    rect_size * field_size, # ширина экрана
    rect_size * field_size # высота экрана
)
game_close = False


# создание и настройка экрана
dis = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake game by Python')