import pygame
from settings import Settings


class Scoreboard:
    def __init__(self, breakout_game):
        pygame.init()
        self.settings = Settings()
        self.turns_left = self.settings.total_lives
        self.score = 0
        self.screen = breakout_game.screen

    def update_score(self):
        self.score += 10
        print(self.score)

    def turn_lost(self):
        if self.turns_left > 0:
            self.turns_left -= 1
            print(self.turns_left)

    def render_scorecard(self):
        self.font = pygame.font.SysFont(
            self.settings.score_font, self.settings.score_size, True, False
        )
        self.score_card = self.font.render(
            f"Score : {str(self.score)}", 1, self.settings.score_color
        )
        self.screen.blit(self.score_card, (1050, 27))

    def render_turns_left(self):
        cnt = 1
        x = 20
        while cnt <= self.turns_left:
            pygame.draw.circle(
                self.screen, self.settings.ball_color, (x, 30), self.settings.ball_size
            )
            x += 20
            cnt += 1
