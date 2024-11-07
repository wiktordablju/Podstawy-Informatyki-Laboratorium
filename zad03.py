import turtle
t = turtle.Turtle()
# t.speed(0)
window = turtle.Screen()


def zad03(bok, min):
    if (bok < min):
        return
    t.forward(bok)
    i = 0
    while i < 6:
        i += 1
        zad03(bok/2, min)
        t.left(60)
    t.backward(bok)


t.left(90)
zad03(200, 100)

window.exitonclick()
