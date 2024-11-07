import turtle
t = turtle.Turtle()
t.speed(0)
window = turtle.Screen()


def zad02(bok, min):
    if (bok < min):
        return
    i = 0
    while i < 2:
        i += 1
        t.forward(bok)
        t.left(90)
        t.forward(bok*3/4)
        t.left(180)
        zad02(bok/2, min)
        t.left(180)
        t.forward(bok/4)
        t.left(90)


zad02(200, 100)
window.exitonclick()
