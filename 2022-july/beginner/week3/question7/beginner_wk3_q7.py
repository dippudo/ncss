from turtle import *
length = int(input("Length? "))

color("pink")
pensize(5)

for i in range(6):
  forward(length)
  left(60)
  backward(length/2)
 
