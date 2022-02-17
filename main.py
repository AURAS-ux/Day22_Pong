import turtle
import Paddle
import Ball
import time
import scoreboard

screen = turtle.Screen()
screen.screensize(canvheight=600, canvwidth=800, bg="black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle.Paddle(350, 0)
paddle2 = Paddle.Paddle(-350, 0)
ball = Ball.Ball()
sb1 = scoreboard.Scoreboard(-200, 280)
sb2 = scoreboard.Scoreboard(200, 280)

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
p1Score = 0
p2Score = 0
game_On = True
while game_On:

    time.sleep(ball.ballSpeed)
    screen.update()
    ball.checkBorderCollision()
    if ball.paddleCollision(paddle1) == 1 or ball.paddleCollision(paddle2) == 1:
        ball.setheading(ball.heading() - 90)
    ball.moveBall()
    if ball.xcor() > 380:
        p1Score += 1
        ball.reset()
        sb1.writeScore(p1Score)
    elif ball.xcor() < -380:
        p2Score += 1
        ball.reset()
        sb2.writeScore(p2Score)
screen.exitonclick()
