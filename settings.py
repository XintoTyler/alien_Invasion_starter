class Settings:
    """A class to store all settings for AlienInvasion Game."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        # Tyler note: I made my screen smaller because of the image i was using, it spawned way too many enemies with default settings
        # I tried scaling the image, but it seemed to mess with the rect way more, so I just scaled the height/width between the spawns
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (90, 90, 90)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self. bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 5
        
        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 3.0
        self.bullet_speed = 5.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)