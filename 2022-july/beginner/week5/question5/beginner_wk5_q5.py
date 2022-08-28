from turtle import *

def move_to(x, y):
  # Move the turtle without drawing
  penup()
  goto(x, y)
  pendown()


def draw_star(size):
  # Draw a star with code
  begin_fill()
  
  right(60)
  forward(size)
  left(120)
  forward(size)
  left(60)
  forward(size)
  left(120)
  forward(size)
  left(120)
  
  end_fill()


# This is our code that draws the Southern Cross.
# It's already correct - you don't need to change it!

# Set the background colour and star colour
bgcolor('black')
pencolor('yellow')
pensize(2)
fillcolor('yellow')
  
# Draw the southern cross
move_to(-10, 80)
draw_star(20)
move_to(-50, 10)
draw_star(18)
move_to(-11, -80)
draw_star(22)
move_to(50, 20)
draw_star(18)
move_to(40, -10)
draw_star(10)
move_to(0, 0)
