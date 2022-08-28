from turtle import *

# Define your function here:
def wheel (red, green, blue):
  for i in range(12):
    fillcolor(red, green, blue)
    
    left(30)
    begin_fill()
    
    forward(50)
    right(60)
    forward(50)
    right(120)
    forward(50)
    right(60)
    forward(50)
    
    right(180)
    forward(20)
    
    red = red - 20
    
    end_fill()


# Test your function
if __name__ == "__main__":
  # Change the values below to see how your pinwheel looks with different colours!
  wheel(220,200,255)
