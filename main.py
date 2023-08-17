import turtle as turtle_module
from turtle import Turtle, Screen
import random


# import colorgram
#
# rgb_list = []
#
# colors = colorgram.extract('hirst_painting.png', 30)
#
# for color in colors:
#     rgb_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_list)

color_list = [(174, 79, 33), (241, 224, 78), (245, 236, 240), (48, 36, 27), (214, 152, 83), (142, 29, 42), (22, 24, 66),
              (44, 44, 117), (166, 22, 16), (51, 86, 154), (208, 87, 128), (152, 52, 85), (126, 161, 217),
              (140, 181, 138), (26, 44, 29), (211, 81, 65), (116, 109, 199), (61, 31, 36), (79, 116, 59),
              (197, 129, 158), (82, 89, 32), (160, 177, 229), (154, 211, 191), (80, 148, 115), (61, 146, 169),
              (198, 136, 50), (56, 101, 21)]


turtle_module.colormode(255)
timmy = Turtle()

timmy.penup()
timmy.hideturtle()
timmy.speed(0)

timmy.setposition(-225.00, -100.00)

for n in range(10):
    y = -250.00 + (n * 50)
    timmy.setposition(-225.00, y)
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)


screen = Screen()
screen.exitonclick()
