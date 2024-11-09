import turtle

# Inicjalizacja zolwia oraz okna
t = turtle.Turtle('turtle')
window = turtle.Screen()
t.speed(0)  # Maksymalna predkosc rysowania

# Ustawienie poczatkowego kata
t.left(60)

# Rekurencyjna funkcja do rysowania fraktalnego szesciokata
def zad01(bok, min):
    # Warunek koncowy rekurencji
    if bok < min:
        return
    # Glowna petla funkcji
    for i in range(6):
        zad01(bok / 3, min)  # Z kazda rekurencja bok zmniejszony jest o 1/3
        t.forward(bok)       
        t.right(60)          

# Wywolanie funkcji z poczatkowa dlugoscia boku 150 i minimalna 50
zad01(150, 50)

# Zamkniecie okna po kliknieciu
window.exitonclick()
