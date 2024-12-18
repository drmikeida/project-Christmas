import pyxel

class ChristmasGame:
    def __init__(self):
        pyxel.init(160,120)
        pyxel.load("my_resource.pyxres")
        self.player_x = 75
        self.player_y = 100
        self.gift_x = pyxel.rndi(0, 150)
        self.gift_y = 0
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < 150:
            self.player_x += 2
        self.gift_y += 2
        if self.gift_y > 120:
            self.gift_x = pyxel.rndi(0, 150)
            self.gift_y = 0
        if abs(self.gift_x - self.player_x) < 10 and abs(self.gift_y - self.player_y) < 10:
            self.score += 1
            self.gift_x = pyxel.rndi(0, 150)
            self.gift_y = 0

    def draw(self):
        pyxel.cls(12)
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 0) # Draws a 16x16 sprite from bank 0
        pyxel.blt(self.gift_x, self.gift_y, 2, 0, 2, 16, 16, 0)  # Draws a 16x16 sprite from bank 0



ChristmasGame()

