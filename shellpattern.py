from turtle import*
pencolor('blue')
pensize(5)
fillcolor('red')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*3)
    lt(25)
    end_fill()
mainloop()