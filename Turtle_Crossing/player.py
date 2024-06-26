from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISCTANCE = 10
FINISH_LINE_Y = 250

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISCTANCE)

    def Finish_race(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False