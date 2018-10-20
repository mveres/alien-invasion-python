class Bullet():
    def __init__(self):
        self.speed_factor = 2
        self.size = 2, 15
        self.color = 244, 176, 66


class Ship():
    def __init__(self):
        self.speed_factor = 2


class Star():
    def __init__(self):
        self.color = 240, 240, 240
        self.size = 1
        self.density = 0.0005  # density of stars across the screen


class Settings():
    def __init__(self):
        self.screen_size = 1200, 800
        self.bg_color = 20, 20, 20
        self.ship = Ship()
        self.star = Star()
        self.bullet = Bullet()
        self.allowed_bullets_no = 5
