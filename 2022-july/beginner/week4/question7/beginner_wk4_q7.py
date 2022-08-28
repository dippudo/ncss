from turtle import *
bgcolor('plum')
fillcolor('cornflowerblue')
pensize(10)
pencolor('royalblue')

slices = int(input("How many sides? "))
angle = 360 / slices

begin_fill()

for i in range(slices):
  forward(40)
  left(angle)

end_fill()
