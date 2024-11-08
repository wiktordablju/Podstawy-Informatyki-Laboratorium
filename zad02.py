import turtle
t = turtle.Turtle('turtle')
# t.speed(0)
window = turtle.Screen()

t.left(90)

def zad02(bok, min):
    if (bok < min):
        return
    for i in range (2):
        # BOK LEWO-PRAWO
        t.forward(bok/4)
        t.left(90)
        zad02(bok/2, min)  
        t.right(90)
        t.forward(3*bok/4)

        # PODSTAWA
        t.right(90)
        t.forward(bok)
        t.right(90)


zad02(200, 200)
window.exitonclick()
