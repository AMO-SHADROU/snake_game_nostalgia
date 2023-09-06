from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.full_snake = []
        self.creat_snake()
        self.head = self.full_snake[0]

    def creat_snake(self):
        for position in STARTING_POSITION:
            self.add_part(position)

    def add_part(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.full_snake.append(snake)

    def extend(self):
        self.add_part(self.full_snake[-1].position())

    def move(self):
        for part in range(len(self.full_snake) - 1, 0, -1):
            new_x = self.full_snake[part - 1].xcor()
            new_y = self.full_snake[part - 1].ycor()
            self.full_snake[part].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
