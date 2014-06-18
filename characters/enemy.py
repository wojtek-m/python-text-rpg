
from character import *

class Enemy(Character):

    def __init__(self, name, health, stamina):
        Character.__init__(self, name, health)
        self.stamina = stamina

tho = Enemy("Tho", 1000, 800)
print tho.name
print tho.health
print tho.stamina
