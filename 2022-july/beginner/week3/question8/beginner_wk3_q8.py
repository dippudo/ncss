from turtle import *
pickets = int(input("How many pickets? "))

color("peru")
pensize(5)

penup()
forward(20)
pendown()
left(90)

for i in range(pickets):
  forward(60)
  backward(60)
  left(90)
  
  penup()
  forward(10)
  right(90)
  pendown()
