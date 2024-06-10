import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, breakout_game):
        super().__init__()
        self.game = breakout_game
        self.settings = breakout_game.game_settings
        self.game_screen = breakout_game.screen
        self.game_screen_rect = breakout_game.screen.get_rect()
        self.player = breakout_game.player
        self.horizontal = "R"
        self.vertical = "U"
        self.collided_against_brick = False

        self.start_pos = (
            self.game_screen_rect.width / 2,
            self.game_screen_rect.height - 40,
        )
        self.curr_pos = self.start_pos
        self.play_ball = pygame.Rect(self.curr_pos[0], self.curr_pos[1], 0, 0)
        self.rect = self.play_ball
        self.blitme()

    def blitme(self):
        self.play_ball = pygame.draw.circle(
            self.game_screen,
            self.settings.ball_color,
            self.curr_pos,
            self.settings.ball_size,
        )

    def get_ball_rect(self):
        return self.play_ball

    def reset_ball(self):
        self.horizontal = "R"
        self.vertical = "U"
        self.settings.ball_speed_factor = 0
        self.curr_pos = self.start_pos
        # self.play_ball = pygame.draw.circle(
        #     self.game_screen,
        #     self.settings.ball_color,
        #     self.start_pos,
        #     self.settings.ball_size,
        # )
        self.blitme()

    def move_ball(self):
        if self.horizontal == "R" and self.vertical == "U":
            self.check_collisions_against_walls()
            self.curr_pos = (
                self.curr_pos[0] + self.settings.ball_speed,
                self.curr_pos[1] - self.settings.ball_speed,
            )
        elif self.horizontal == "R" and self.vertical == "D":
            self.check_collisions_against_walls()
            self.curr_pos = (
                self.curr_pos[0] + self.settings.ball_speed,
                self.curr_pos[1] + self.settings.ball_speed,
            )
        elif self.horizontal == "L" and self.vertical == "U":
            self.check_collisions_against_walls()
            self.curr_pos = (
                self.curr_pos[0] - self.settings.ball_speed,
                self.curr_pos[1] - self.settings.ball_speed,
            )
        elif self.horizontal == "L" and self.vertical == "D":
            self.check_collisions_against_walls()
            self.curr_pos = (
                self.curr_pos[0] - self.settings.ball_speed,
                self.curr_pos[1] + self.settings.ball_speed,
            )
        self.blitme()

    def check_collisions_against_walls(self):
        # Collision with the right Wall. Result - > Bounce back to Left
        if (
            self.curr_pos[0] >= self.game_screen_rect.width - 20
            and self.horizontal == "R"
        ):
            self.horizontal = "L"
        # Collision with the left Wall. Result - > Bounce back to right
        elif self.curr_pos[0] <= 10 and self.horizontal == "L":
            self.horizontal = "R"

        # Collision with the top Wall. Result - > Bounce back to bottom
        elif self.curr_pos[1] <= 10 and self.vertical == "U":
            self.vertical = "D"

        # Collision with the player. Ball bounes back
        elif (
            self.player.player_rect.colliderect(self.play_ball) and self.vertical == "D"
        ):

            self.vertical = "U"
        # collision with bottom wall
        elif self.curr_pos[
            1
        ] >= self.game_screen_rect.height - 5 and not self.player.player_rect.colliderect(
            self.play_ball
        ):

            self.game.game_reset = True
            self.player.reset_player()
            self.reset_ball()
            self.game.score.turn_lost()

        # Collison with the bricks
        elif self.collided_against_brick:
            self.vertical = "D"
            self.collided_against_brick = False

    def check_collisions_against_player(self):
        self.player.player_rect.colliderect(self.play_ball)

    # def check_collisions_against_bricks(self):
    #     pygame.sprite.spritecollide(self.ball_sprite, self.brick_wall, True)
