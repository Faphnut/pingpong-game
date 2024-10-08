import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
my_turtle = turtle.Turtle()

# Set the turtle properties
my_turtle.color("white", "blue")  # Set pen color to white and fill color to blue
my_turtle.pensize(2)  # Set pen size
my_turtle.speed(2)  # Set drawing speed

# Draw the filled square with blue stroke
my_turtle.penup()  # Lift the pen to move without drawing
my_turtle.goto(-20, -20)  # Move to the starting position
my_turtle.pendown()  # Lower the pen to start drawing

my_turtle.begin_fill()  # Begin filling the shape
for _ in range(4):
    my_turtle.forward(40)
    my_turtle.right(90)
my_turtle.end_fill()  # End filling the shape

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open
turtle.mainloop()
