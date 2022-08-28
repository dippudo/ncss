from turtle import *

def draw_branch():
  forward(50)
  left(60)
  for i in range(6):
    forward(15)
    right(60)
  right(60)
  backward(50)

# Write your code below!
bgcolor('darkblue')
pensize(2)
pencolor('white')
fillcolor('white')

branches = int(input("How many branches? "))

angle = 360 / branches

begin_fill()

for i in range(branches):
  draw_branch()
  right(angle)

end_fill()
