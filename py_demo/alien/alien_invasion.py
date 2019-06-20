import pygame

from alien.game_functions import check_events
from alien.settings import Settings
from alien.ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()

    # 设置屏幕大小
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 设置背景颜色
    bg_color = ai_setting.bg_color

    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        check_events()
        update_screen(bg_color, screen, ship)


def update_screen(bg_color, screen, ship):
    # 每次循环时都重绘屏幕
    screen.fill(bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


run_game()
