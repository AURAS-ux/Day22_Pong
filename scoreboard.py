import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.hideturtle()
        self.goto(xpos, ypos)
        self.color("white")
        self.write(f"Player score:{0}", align="center", font=("Arial", 20, "bold"))

    def writeScore(self, score):
        self.clear()
        self.write(f"Player score:{score}", align="center", font=("Arial", 20, "bold"))
