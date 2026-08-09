from Enemies import Enemies

class Goblin(Enemies):
    def __init__(self):
        super().__init__("Goblin",50, 5, 25, 4)