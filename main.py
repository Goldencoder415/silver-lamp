import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.title("Turtle Shapes Demo")

# Create a turtle
t = turtle.Turtle()
t.speed(2)  # Set the drawing speed
# Function to draw a star
def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)
# Draw a star
t.color("purple")
t.penup()
t.goto(50, -100)
t.pendown()
draw_star(100)
# Hide the turtle and keep the window open
t.hideturtle()
screen.mainloop()
