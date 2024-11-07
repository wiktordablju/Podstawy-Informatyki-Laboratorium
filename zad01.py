import turtle
t = turtle.Turtle()
t.speed(0)
window = turtle.Screen()


def zad01(bok, min):
    if (bok < min):
        return
    i = 0
    while i < 6:
        i += 1
        zad01(bok/3, min)
        t.forward(bok)
        t.left(60)


zad01(150, 50)

window.exitonclick()
