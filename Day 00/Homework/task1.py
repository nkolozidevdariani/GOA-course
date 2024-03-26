from turtle import *

speed(100)
#კედლები
width(5)
color("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

#კარები
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)
end_fill()

penup()
goto(200, 200)
pendown()

#სახურავი
color("purple")
begin_fill()
right(50)
forward(150)
left(97)
forward(150)
left(133)
forward(200)
end_fill()

penup()
goto(70, 130)
pendown()

#ფანჯარა
color("blue")
begin_fill()
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
end_fill()

exitonclick()