class Turtle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self, steps):
        final_position = self.x - steps
        if final_position < 0:
            final_position = 0
        self.x = final_position

    def move_right(self, steps):
        final_position = self.x + steps
        if final_position > 10:
            final_position = 10
        self.x = final_position

    def move_up(self, steps):
        final_position = self.y + steps
        if final_position > 10:
            final_position = 10
        self.y = final_position

    def move_down(self, steps):
        final_position = self.y - steps
        if final_position < 0:
            final_position = 0
        self.y = final_position

    def get_position(self):
        return self.x, self.y


myturtle = Turtle(3, 3)
myturtle.move_left(5)
myturtle.move_up(5)
print(myturtle.get_position())
