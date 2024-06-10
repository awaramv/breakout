import pygame
from settings import Settings
from player import Player
from ball import Ball
from bricks import Bricks
from pygame.sprite import Group
from scorecard import Scoreboard


class Breakout_Game:
    def __init__(self):
        pygame.init()
        self.game_settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.game_settings.screen_width, self.game_settings.screen_height)
        )

        self.clock = pygame.time.Clock()
        self.game_active = True
        self.game_reset = False
        self.player = Player(self)
        self.ball = Ball(self)
        self.ball_sprite = Group()
        self.ball_sprite.add(self.ball)
        self.brick_wall = Group()
        self.create_brick_wall()
        self.score = Scoreboard(self)

    def create_brick_wall(self):
        row = 1
        new_x = 40
        new_y = 60
        while row < 8:
            if new_x <= self.game_settings.screen_width - 40 and row < 8:
                new_brick = Bricks(self, new_x, new_y)
                self.brick_wall.add(new_brick)

                new_x = new_x + self.game_settings.brick_width + 2
            elif new_x >= self.game_settings.screen_width - 40:
                row += 1
                new_y += self.game_settings.brick_height + 2
                new_x = 40

    def restart_game(self):
        self.game_reset = False

    def event_listener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_active = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_left = True
                    self.player.move_player()
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right = True
                    self.player.move_player()
                elif event.key == pygame.K_SPACE:
                    self.restart_game()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.move_left = False
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right = False

    def update_screen(self):
        self.screen.fill("purple")

        if self.game_active:
            for brick in self.brick_wall.sprites():
                brick.create_brick()
        self.player.blitme()
        self.event_listener()
        if not self.game_reset:
            self.ball.move_ball()
        else:
            self.ball.reset_ball()
            self.player.reset_player()

        for brick in self.brick_wall.sprites():
            collision = self.ball.play_ball.colliderect(brick.rect)

            if collision:
                self.brick_wall.remove(brick)
                print(self.brick_wall)
                self.ball.move_ball()
                self.ball.collided_against_brick = True
                self.score.update_score()
        self.score.render_scorecard()
        self.score.render_turns_left()
        self.clock.tick(120)
        pygame.display.flip()

    def execute_game(self):
        while self.game_active:
            self.update_screen()


if __name__ == "__main__":
    new_game = Breakout_Game()
    new_game.execute_game()
