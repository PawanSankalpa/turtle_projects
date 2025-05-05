
from random import choice
import turtle as turtle_module

color_list = [ (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]


t = turtle_module.Turtle()
turtle_module.colormode(255)
t.speed("fastest")
t.hideturtle()

def move():
    t.forward(17)
    for _ in range(14):
        #tutle.dot (size,color)
        t.dot(20,choice(color_list))
        t.penup()
        t.forward(50)
    t.backward(717) #(15*14)+17 =717
    t.setheading(90)
    t.forward(50)
    t.setheading(0)



def starting_point():
    for _ in range(7):
        t.penup()
        t.backward(50)
    for _ in range(6):
        t.setheading(270)
        t.forward(50)
    t.setheading(0)








starting_point()
for _ in range(14):
    move()



screen = turtle_module.Screen()
screen.exitonclick()