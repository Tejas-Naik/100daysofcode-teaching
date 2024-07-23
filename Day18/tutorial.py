import random
from turtle import Turtle, Screen

mike = Turtle()
screen = Screen()
mike.speed("fastest")

# colours = ['skyblue', 'red', 'green', 'black', 'white', 'orange']

# for i in range(360):
#     # mike.color(colours[0] if i % 2 == 0 else colours[1] )
#     mike.color(random.choice(colours))
#     mike.circle(100)
#     mike.right(1)

mike.setheading(225)
mike.forward(100)
mike.dot(20)
mike.setheading(0)
mike.dot(20)
mike.forward(20)
mike.dot(20)
screen.exitonclick()