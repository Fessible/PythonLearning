import pygame


class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 放置位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 是否移动
        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
