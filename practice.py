from multiprocessing.spawn import import_main_path


import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed('fastest')
temp=1
clrlist=["red","green","yellow"]
for i in range(400):
    t.color(clrlist[i%3])
    t.left(120)
    t.left(1)
    temp=temp+1
    t.forward(temp)
turtle.mainloop()
