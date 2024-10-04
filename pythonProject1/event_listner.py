from turtle import Turtle, Screen

timmy = Turtle()
sc = Screen()


def front():
    timmy.forward(10)


def back():
    timmy.backward(10)


def left():
    n = timmy.heading() + 10
    timmy.setheading(n)


def right():
    n = timmy.heading() - 10
    timmy.setheading(n)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()#return to 00 cordinate
    timmy.pendown()




sc.listen()
sc.onkey(front, "w")
sc.onkey(back, "s")
sc.onkey(left, "a")
sc.onkey(right, "d")
sc.onkey(clear, "space")

sc.exitonclick()
