from turtle import *

# Put your function here
def draw_hexagon(x, y, colour):
  penup()
  goto(x, y)
  
  pendown()
  fillcolor(colour)
  begin_fill()
  
  forward(30)
  right(60)
  forward(30)
  right(60)
  forward(30)
  right(60)
  forward(30)
  right(60)
  forward(30)
  right(60)
  forward(30)
  right(60)
  
  end_fill()


speed(3)
# Our code to draw hexagonal honeycomb
bgcolor('darkorange')
pensize(4)
pencolor('orange4')
draw_hexagon(-15, 48, 'gold2')
draw_hexagon(-15, -4, 'goldenrod')
draw_hexagon(-60, 74, 'yellow2')
draw_hexagon(-60, 22, 'gold')
draw_hexagon(-60, -30, 'yellow')
draw_hexagon(30, 22, 'yellow')
