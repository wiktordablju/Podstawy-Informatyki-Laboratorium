import turtle
t = turtle.Turtle('turtle')
# t.speed(0)
window = turtle.Screen()

t.left(90)

def zad03(bok, min):
    if (bok < min):
        return
    
    t.forward(bok) 
    i = 0
    while i < 6:
        i += 1
        zad03(bok/2, min)
        t.right(60)
    t.backward(bok)



zad03(200, 100)

window.exitonclick()
