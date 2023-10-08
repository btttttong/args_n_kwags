import turtle as t
import random as r

bob = t.Turtle()

screen = t.Screen()
screen.listen()

screen.setup(width=500, height=500)
bob.penup()
bob.goto(-240, -240)


def go_up():
    bob.setheading(90)
    bob.forward(10)


def go_down():
    bob.setheading(270)
    bob.forward(10)


def go_left():
    bob.setheading(180)
    bob.forward(10)


def go_right():
    bob.setheading(0)
    bob.forward(10)


def pen_up():
    if bob.isdown():
        bob.penup()
    else:
        bob.pendown()

def change_color():
    color = ('red', 'magenta', 'blue', 'cyan', 'green', 'black', 'yellow')
    bob.pencolor(r.choice(color))

def clear_scrn():
    bob.clear()


screen.onkeypress(fun=go_up, key="Up")
screen.onkeypress(fun=go_down, key="Down")
screen.onkeypress(fun=go_left, key="Left")
screen.onkeypress(fun=go_right, key="Right")
screen.onkeypress(fun=pen_up, key="p")
screen.onkeypress(fun=change_color, key="c")
screen.onkeypress(fun=clear_scrn, key="-")

bob.screen.mainloop()
