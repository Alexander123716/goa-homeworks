from turtle import *

#we want to paint a house 

#step:1 draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#draving a dor

forward(70)
color("yellow")
left(90)
forward(120)  #height of the dor
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,  200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()



penup()
goto(20,180)
pendown()
left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
penup()
goto(180,180)
pendown()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
