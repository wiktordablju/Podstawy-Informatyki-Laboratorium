import turtle
t = turtle.Turtle('turtle')
# t.speed(0)
window = turtle.Screen()

t.left(60)
def zad01(bok, min):
    if (bok < min):
        return
    i = 0
    while i < 6:
        i += 1
        zad01(bok/3, min)
        t.forward(bok)
        t.right(60)


zad01(150, 50)

window.exitonclick()
