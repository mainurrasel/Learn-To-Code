import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.color('blue')

pokey = turtle.Turtle()
pokey.shape('turtle')
pokey.color('red')

rokey = turtle.Turtle()
rokey.shape('turtle')
rokey.color('green')

def make_square(the_turtle):
    for i in range (0,4):
        the_turtle.forward(100)
        the_turtle.right(90)
        
def make_spiral(the_turtle):
    for i in range(0, 36):
        make_square(the_turtle)
        the_turtle.right(10)

make_spiral(slowpoke)
pokey.right(5)
make_spiral(pokey)
rokey.right(2.5)
make_spiral(rokey)

turtle.mainloop()
