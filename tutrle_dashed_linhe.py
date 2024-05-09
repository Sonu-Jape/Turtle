import turtle as t
from turtle import Screen
import random


tim = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]
def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3 , 11):
    tim.color(random.choice(colours))
    draw_shapes(shape_side_n)


#
# for _ in range(1000):
#
#
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
screen = Screen()
screen.exitonclick()