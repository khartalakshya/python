from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

sc = Screen()
sc.setup(800, 600)
sc.bgcolor("black")
sc.title("pong_game")
sc.tracer(0)  # here i had turn off  the animation

# timmy = Turtle()
p1 = Paddle(350, 0)
p2 = Paddle(-350, 0)
b1 = Ball()
scr1 = Score()


sc.listen()
sc.onkey(p1.go_up, "Up")
sc.onkey(p1.go_dw, "Down")
sc.onkey(p2.go_up, "w")
sc.onkey(p2.go_dw, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.09)
    sc.update()
    b1.move()
    if b1.distance(p1) < 50 and b1.xcor() > 320:
        b1.bounce('X')
    if b1.distance(p2) < 50 and b1.xcor() < -320:
        b1.bounce('X')
    if (b1.ycor() > 280) or (b1.ycor() < -280):
        b1.bounce('Y')

    if b1.xcor() > 380:
        #playe 1 win the game
        b1.restar()
        scr1.l_point()

    if b1.xcor() < -380:
        #playe 2 win the game
        scr1.r_point()
        b1.restar()

sc.exitonclick()
