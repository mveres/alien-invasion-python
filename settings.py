class Bullet():
    def __init__(self):
        self.speed_factor = 10
        self.size = 2, 15
        self.color = 244, 176, 66


class Ship():
    def __init__(self):
        self.speed_factor = 8
        self.limit = 3


class Star():
    def __init__(self):
        self.color = 240, 240, 240
        self.size = 1
        self.density = 0.0005  # density of stars across the screen


class Alien():
    def __init__(self):
        self.speed_factor = 5
        self.fleet_drop_speed = 10
        self.fleet_initial_direction = 1  # 1 = left, -1 = right


class Settings():
    def __init__(self):
        self.screen_size = 1200, 800
        self.bg_color = 20, 20, 20
        self.ship = Ship()
        self.star = Star()
        self.alien = Alien()
        self.bullet = Bullet()
        self.allowed_bullets_no = 5
