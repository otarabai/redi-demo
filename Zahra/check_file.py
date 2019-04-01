# Test file

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

#ctrl+t
#ctrl+k