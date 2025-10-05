import turtle


screen = turtle.Screen()
screen.bgcolor("white") # Set background color


t = turtle.Turtle()
t.color("blue")


for i in range(36): # 36 times for a circular pattern (360/10)
    t.forward(100)
    t.left(10)


t.penup()
t.goto(25, 50)
t.write("hello!" , align="center", font=("Arial", 16, "normal"))


screen.exitonclick()
