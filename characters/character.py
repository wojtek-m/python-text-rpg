
class Character(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

        self.dead = False

    def attack(self, other):
        pass

    def update(self):
        if self.health < 0:
            self.dead = True