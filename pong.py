from turtle import Turtle, Screen
from time import sleep
from random import randint, choice


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.goto(x_cor, y_cor)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 40)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 40)


class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x_move = x
        self.y_move = y

        self.shape("circle")
        self.speed(5)
        self.penup()
        self.shapesize(1, 1)
        self.color("white")

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_from_wall(self):
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move += randint(-4, 4)
        self.x_move *= -1
        self.y_move += randint(-4, 4)


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball(randint(-4, 4), randint(-4, 4))
# ball1 = Ball(randint(-4, 4), randint(-4, 4))
game_is_on = True

while game_is_on:

    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_from_wall()
    if paddle1.xcor() - 20 <= ball.xcor() <= paddle1.xcor() + 20 and \
            paddle1.ycor() - 50 <= ball.ycor() <= paddle1.ycor() + 50 or \
            paddle2.xcor() - 20 <= ball.xcor() <= paddle2.xcor() + 20 and \
            paddle2.ycor() - 50 <= ball.ycor() <= paddle2.ycor() + 50:
        ball.bounce_from_paddle()
    if ball.xcor() >= 450 or ball.xcor() <= -450:
        game_is_on = False
    if abs(ball.y_move) >= 8 or abs(ball.y_move) <= 3:
        ball.y_move = choice([5, -5])

    # For second ball
    # ball1.move()
    # if ball1.ycor() >= 280 or ball1.ycor() <= -280:
    #     ball1.bounce_from_wall()
    # if paddle1.xcor() - 20 <= ball1.xcor() <= paddle1.xcor() + 20 and \
    #         paddle1.ycor() - 50 <= ball1.ycor() <= paddle1.ycor() + 50 or \
    #         paddle2.xcor() - 20 <= ball1.xcor() <= paddle2.xcor() + 20 and \
    #         paddle2.ycor() - 50 <= ball1.ycor() <= paddle2.ycor() + 50:
    #     ball1.bounce_from_paddle()
    # if ball1.xcor() >= 450 or ball1.xcor() <= -450:
    #     game_is_on = False
    # if abs(ball1.y_move) >= 8 or abs(ball1.y_move) <= 3:
    #     ball1.y_move = choice([5, -5])

    screen.update()
    screen.listen()
    sleep(0.02)
    screen.onkey(paddle1.move_up, "Up")
    screen.onkey(paddle1.move_down, "Down")
    screen.onkey(paddle2.move_up, "w")
    screen.onkey(paddle2.move_down, "s")
screen.bgcolor("red")
screen.exitonclick()
