from turtle import Turtle,Screen
from random import randint

screen=Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle win the race? Enter a color: \n'red','pink','orange','black','green','blue'")
race_is_on =True
color_list = ["red","pink","orange","black","green","blue"]
distance_list = [80,40,0,-40,-80,-120]
turtle_list =[]

for turtle_index in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(color_list[turtle_index])
    new_turtle.goto(x=-235,y=distance_list[turtle_index])
    turtle_list.append(new_turtle)

while race_is_on:
    for the_turtle in turtle_list:

        if the_turtle.xcor() > 230:
            race_is_on = False
            if the_turtle.pencolor() == user_bet.lower():
                print(f"You got it correct! the winning turtle color is {the_turtle.pencolor()}")
            else:
                print(f"You got it wrong! the winning turtle color is {the_turtle.pencolor()}")

        the_turtle.forward(randint(0, 10))





screen.exitonclick()