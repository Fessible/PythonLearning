import pygame
import sys
from alien_invasion.settings import Settings
from alien_invasion.ship import Ship
from alien_invasion.game_function import check_events


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()

    # 设置屏幕大小
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(screen,ai_setting)

    pygame.display.set_caption("Alien Invasion")

    # 设置背景颜色
    bg_color = ai_setting.bg_color

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        check_events(ship)
        update_screen(screen, bg_color, ship)


def update_screen(screen, bg_color, ship):
    # 每次循环时都重绘屏幕
    screen.fill(bg_color)

    ship.blitme()
    ship.update()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


run_game()
