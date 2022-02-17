import turtle
import random

class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.shapesize(1, 1)
        self.setheading(45)
        self.ballSpeed = 0.095

    def moveBall(self):
        self.forward(20)

    def checkBorderCollision(self):
        if self.ycor() > 270 or self.ycor() < -300:
            self.setheading(self.heading() - 90)

    def paddleCollision(self, paddle):
        if self.xcor() > 320 or self.xcor() < -320:
            if self.distance(paddle) < 50:
                self.ballSpeed *= 0.9
                return 1

    def reset(self):
        self.goto(0, 0)
        self.setheading(random.randint(0,90))
