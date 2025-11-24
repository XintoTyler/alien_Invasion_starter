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
        self.ship_speed = 3.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self. bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 5
        
        # Alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 15
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1