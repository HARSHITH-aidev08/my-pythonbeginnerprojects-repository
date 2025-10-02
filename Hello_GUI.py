import turtle

# Create a screen
screen = turtle.Screen()
screen.bgcolor("white") # Set background color

# Create a turtle object
t = turtle.Turtle()
t.color("blue")

# Draw something with a loop
for i in range(36): # 36 times for a circular pattern (360/10)
    t.forward(100)
    t.left(10)

# Lift the pen and move to center
t.penup()
t.goto(25, 50)
t.write("hello!" , align="center", font=("Arial", 16, "normal"))

# Wait for user click to exit
screen.exitonclick()
