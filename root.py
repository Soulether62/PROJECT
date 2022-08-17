import turtle as tk 
ro=tk.Turtle()
wn=tk.Screen()
wn.bgcolor("black")
ro.left(90)
ro.speed(1000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(3*l/4)
        ro.right(60)
        draw(3*l/4)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(20)
ro.right(90)
ro.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(3*l/4)
        ro.right(60)
        draw(3*l/4)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(20)
ro.right(270)
ro.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(3*l/4)
        ro.right(60)
        draw(3*l/4)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(20)
ro.right(90)
ro.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("#FFF8DC")
        ro.forward(l)
        ro.left(30)
        draw(3*l/4)
        ro.right(60)
        draw(3*l/4)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(20)


def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(3)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(4*l/5)
        ro.right(60)
        draw(4*l/5)
        ro.left(30)
        ro.pensize(3)
        ro.backward(l)

draw(40)
ro.right(90)
ro.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(4*l/5)
        ro.right(60)
        draw(4*l/5)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(40)
ro.right(270)
ro.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(4*l/5)
        ro.right(60)
        draw(4*l/5)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(40)
ro.right(90)
ro.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(4*l/5)
        ro.right(60)
        draw(4*l/5)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(40)


def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(6*l/7)
        ro.right(60)
        draw(6*l/7)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(60)
ro.right(90)
ro.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(6*l/7)
        ro.right(60)
        draw(6*l/7)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(60)
ro.right(270)
ro.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(6*l/7)
        ro.right(60)
        draw(6*l/7)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(60)
ro.right(90)
ro.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(6*l/7)
        ro.right(60)
        draw(6*l/7)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(60)
wn.exitonclick()
