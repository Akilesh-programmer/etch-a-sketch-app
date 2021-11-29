# W - forwards
# S - backwards
# A - Counter-Clockwise
# D - Clockwise
# C - Clear all the drawing and put the turtle back in the center.

# Importing turtle class.
import turtle as t

# Creating a object named akilesh from turtle object.
akilesh = t.Turtle()

# Creating a screen object from turtle to view the output.
screen = t.Screen()

# Creating a function to move forwards.
def forwards():
    akilesh.forward(10)

# Creating a function to move backwards.
def backwards():
    akilesh.back(10)

# Creating a function to turn clockwise.
def turn_clockwise():
    akilesh.right(90)

# Creating a function to turn counter - clockwise.
def turn_counter_clockwise():
    akilesh.left(90)

# Creating a function to clear the screen and bring the turtle to the initial position.
def clear_screen():
    akilesh.clear()
    akilesh.reset()

# Calling a method to listen to the user.
screen.listen()

# Calling a method to move the turtle forwards.
screen.onkey(key="w", fun=forwards)

# Calling a method to move the turtle backwards.
screen.onkey(key="s", fun=backwards)

# Calling a method to turn the turtle clockwise.
screen.onkey(key="d", fun=turn_clockwise)

# Calling a method to turn the turtle counter clockwise.
screen.onkey(key="a", fun=turn_counter_clockwise)

# Calling a method to clear the screen.
screen.onkey(key="c", fun=clear_screen)

# Using a metod associated with screen to make the screen stay and then exit when we click on it.
screen.exitonclick()