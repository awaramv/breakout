import pygame


class Player:
    def __init__(self, breakout_game):
        self.settings = breakout_game.game_settings
        self.game_screen = breakout_game.screen
        self.game_screen_rect = breakout_game.screen.get_rect()

        self.player_rect = pygame.Rect(
            self.game_screen_rect.width / 2,
            self.game_screen_rect.height - 20,
            self.settings.player_width,
            self.settings.player_height,
        )
        self.x = self.player_rect.x
        self.player_rect.midbottom = self.game_screen_rect.midbottom
        self.move_right = False
        self.move_left = False

    def blitme(self):
        # self.game_screen.blit(self.player_slab, self.player_rect)
        pygame.draw.rect(self.game_screen, self.settings.player_color, self.player_rect)

    def move_player(self):

        if (
            self.move_right
            and self.player_rect.x
            <= self.game_screen_rect.width - self.player_rect.width
        ):
            self.player_rect.x += 30
        elif self.move_left and self.player_rect.left >= 25:
            self.player_rect.x -= 30
        self.blitme()
        # self.game_screen.blit(self.player_slab, self.player_rect)

    def reset_player(self):
        self.player_rect.midbottom = self.game_screen_rect.midbottom
        self.blitme()
