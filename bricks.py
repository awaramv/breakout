import pygame
from pygame.sprite import Sprite


class Bricks(Sprite):
    def __init__(self, breakout_game, x, y):
        super().__init__()
        pygame.init()
        self.settings = breakout_game.game_settings
        self.game_screen = breakout_game.screen
        self.game_screen_rect = breakout_game.screen.get_rect()
        self.brick_width = self.settings.brick_width
        self.brick_height = self.settings.brick_height
        self.xpos = x
        self.ypos = y
        self.rect = pygame.Rect(
            self.xpos, self.ypos, self.brick_width, self.brick_height
        )

    #    (
    #         self.game_screen,
    #         (150, 75, 0),
    #         (self.xpos, self.ypos, self.brick_width, self.brick_height),
    #     )

    def create_brick(self):
        self.brick = pygame.draw.rect(
            self.game_screen,
            (150, 75, 0),
            self.rect,
        )

    # def get_brick(self):
    #     return self.brick
