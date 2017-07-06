from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)
color = input("What color do you want?")
pendown()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
penup()
left(120)
back(60)
pendown()
back(100)
right(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
t.fillcolor(f"{color}")
### Write your code below:






# Close window on click.
exitonclick()
