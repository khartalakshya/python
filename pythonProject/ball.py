from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        xcor = self.xcor() + self.x
        ycor = self.ycor() + self.y
        self.goto(xcor, ycor)

    def bounce(self, ch):
        if ch == 'X':
            self.x = self.x * -1
        elif ch== 'Y':
            self.y = self.y * -1

    def restar(self):
        self.goto(0,0)
