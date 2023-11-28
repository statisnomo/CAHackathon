import turtle
import time

# Create screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create nucleus
nucleus = turtle.Turtle()
nucleus.shape("circle")
nucleus.color("yellow")

# Create orbital
orbital = turtle.Turtle()
orbital.color("blue")
orbital.penup()
orbital.goto(0, -100)
orbital.pendown()
orbital.circle(100)

# Create electron
electron = turtle.Turtle()
electron.shape("circle")
electron.color("white")
electron.penup()
electron.goto(0, -100)

# Move electron in orbital
while True:
    electron.circle(100, 10)
    time.sleep(0.1)

# This will keep the screen open until it is clicked
turtle.done()