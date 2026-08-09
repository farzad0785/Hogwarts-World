from Enemies import Enemies

class Wolf(Enemies):
    def __init__(self):
        super().__init__("Wolf", 200, 20, 100, 20)