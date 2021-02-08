import turtle
#Star
slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.color('blue')
'''
for i in range(5):
    slowpoke.forward(100)
    slowpoke.right(144)
'''
#Two Circle
'''
slowpoke.pencolor('blue')
slowpoke.penup()
slowpoke.setposition(-120, 0)
slowpoke.pendown()
slowpoke.circle(50)
slowpoke.pencolor('red')
slowpoke.penup()
slowpoke.setposition(120, 0)
slowpoke.pendown()
slowpoke.circle(50)
'''
#Make Shape
'''
def make_shape(t, sides):
    angle = 360/sides
    for i in range(0, sides):
        t.forward(100)
        t.right(angle)

#make_shape(slowpoke, 1)
#make_shape(slowpoke, 2)
make_shape(slowpoke, 3)
make_shape(slowpoke, 5)
make_shape(slowpoke, 8)
make_shape(slowpoke, 10)
'''

turtle.mainloop()
