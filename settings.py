class Settings:
    def __init__(self):
        # Screen level Settings
        self.screen_width = 1200
        self.screen_height = 800

        # Player level settings
        self.player_speed = 1
        self.player_color = (150, 75, 0)
        self.player_height = 20
        self.player_width = 100

        # Ball level settings
        self.initial_ball_speed = 2
        self.ball_speed_factor = 1
        self.ball_speed = self.initial_ball_speed * self.ball_speed_factor
        self.ball_color = (255, 255, 255)
        self.ball_size = 10

        # Brick level settings
        self.brick_color = (150, 75, 0)
        self.brick_vertical_speed = 1
        self.brick_width = 50
        self.brick_height = 30

        # Score_card settings
        self.score_font = ("Arial",)
        self.score_color = (255, 255, 255)
        self.score_size = 24

        # Game Settings
        self.total_lives = 3
