
from character import *

class Player(Character):
    def __init__(self, name, health, stamina):
        Character.__init__(self, name, health)
        self.stamina = stamina