import turtle


class Paddle(turtle.Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(xpos, ypos)
        self.color("white")
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
