from turtle import *

# Define your function here!
def firework(colour, x, y):
  pensize(4)
  pencolor(colour)
  
  penup()
  goto(0, -150)
  
  pendown()
  goto(x, y)
  
  for i in range(10):
    forward(50)
    forward(-50)
    right(36)




# Call your function here to draw the four fireworks
# We've started you off with the background and 2 fireworks
bgcolor('#000000') 
firework('#0085C7', 30, 40)
firework('#009F3D', -50, 80)
# Draw the yellow and red fireworks by calling your function here
firework('#F4C300', -50, -40)
firework('#DF0024', 40, -60)
