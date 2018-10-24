class GameStats():

    def __init__(self, settings):
        self.ship_limit = settings.ship.limit
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ship_limit

    def decrease_ships_left(self):
        self.ships_left -= 1
