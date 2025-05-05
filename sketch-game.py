from turtle import Turtle,Screen


tim = Turtle()
screen =Screen()

"""Old one before updating"""
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#    tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
#
# def clear_the_screen():
#     tim.clear()
#     tim.pen()
#     tim.home()
"""-----------------------"""
"""Old one, before updating"""
# screen.listen()
# screen.onkey(key='w', fun=move_forwards)
# screen.onkey(key='s', fun=move_backwards)
# screen.onkey(key='a', fun=turn_left)
# screen.onkey(key='d',fun=turn_right)
# screen.onkey(key='c',fun=clear_the_screen)
""" ----------------------------------"""

'''not finished , the output is is not satisfactory'''
'''need to figure out how to do both keys at the same time.'''
'''ex : a and w to draw a circle counterclockwise'''

'''---Then let's talk about the logic.---'''
"""Right now , once we press the key, it functions . But it can't tell whether we hold multiple keys or not"""

# First we can create a function called move(), where it can check, the key your holding,
# then move according to it. but it should check it within a very short time period repeatedly.

# Let's create a basket that can hold which keys we are pressing right now.
pressed_keys = set() #Why do we use set here instead of lists, because set won't allow duplicates, unlike lists.

def move():
    if "w" in pressed_keys:
        tim.forward(5) #reduce the moving amount because it checks the function in a short time period repeatedly.
    if "s" in pressed_keys:
        tim.backward(5)
    if "a" in pressed_keys:
        tim.left(5)
    if "d" in pressed_keys:
        tim.right(5)
    #check this again and again in a short time period.
    screen.ontimer(move, 50) # Repeat every 50ms

#This function, to add the current holding keys to the pressed key set,
def key_press(key):
    pressed_keys.add(key)

#This function, to remove the release key from the pressed key set,
def key_release(key):
    pressed_keys.remove(key)

#This function, to clear the screen
def clear_the_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

"""What is an anonymous function : a function that doesn't have a name"""
"""In python, lambda is a way to create small, anonymous functions"""

screen.listen()

# Set up Key controls(press)
screen.onkeypress(lambda : key_press("w"), key="w")
screen.onkeypress(lambda : key_press("s"), key="s")
screen.onkeypress(lambda : key_press("a"), key="a")
screen.onkeypress(lambda : key_press("d"), key="d")

# Set up Key Controls(release)
screen.onkeyrelease(lambda : key_release("w"), key="w")
screen.onkeyrelease(lambda : key_release("s"), key="s")
screen.onkeyrelease(lambda : key_release("a"), key="a")
screen.onkeyrelease(lambda : key_release("d"), key="d")

screen.onkey(clear_the_screen, key="c")

move()


screen.exitonclick()