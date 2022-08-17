import turtle
colors=["red","purple","green","orange","blue","yellow"]
t= turtle.Pen()
turtle.bgcolor("black")
t.speed('fastest')
for x in range(360):
    t.hideturtle()
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)
    
    