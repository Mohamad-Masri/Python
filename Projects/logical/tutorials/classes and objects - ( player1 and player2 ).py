class Player :
    energy = 100

    def eat_apple (self):
        self.energy += 10

    def eat_orange (self) :
        self.energy -=15

player1 = Player()
player2 = Player()

player1.eat_apple()
player2.eat_orange()

print (player1.energy)
print (player2.energy)
