from turtle import Turtle
STARTING_POSITIONS = [(0,-40),(0,-20),(0,0),(0,20),(0,40)]

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segments= []
        self.create_paddle()

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

