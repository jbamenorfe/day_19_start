# Write a turtle program that allows the user to draw a circle or any polygon using the following keys:
# (a)   W = Move Forward
# (b)   S = Move Backward
# (c)   A = Counerclockwise (Move Left)
# (d)   D = Clockwise (Move Right)
# (e)   C = Clear drawing

from turtle import Turtle, Screen
tonny = Turtle()

# Write functions for the keys
def move_forward():
    tonny.forward(5)

def move_backward():
    tonny.backward(5)

def rotate_counterclockwise():
    tonny.left(10)

def rotate_clockwise():
    tonny.right(10)

def clear_drawing():
    tonny.clear()
    tonny.penup()
    tonny.home()
    tonny.pendown()

# Call the various functions and assign them to keys
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_drawing)



screen.exitonclick()