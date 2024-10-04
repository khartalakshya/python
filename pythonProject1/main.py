import random
from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
sc = Screen()

timmy.speed("fastest")
sc.colormode(255)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
num_of_dots = 100
timmy.penup()

color_list = [(62, 7, 24), (189, 6, 30), (8, 26, 58), (193, 64, 23), (249, 57, 22), (249, 246, 207)]

for dits in range(1, num_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dits % 10 == 0:
        timmy.setheading(90)
        timmy.fd(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


sc.exitonclick()
