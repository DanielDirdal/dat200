import turtle


# Eksempel på en fraktal: Rekursivt program som tegner et enkelt tre.
def tegn_tre(lengde, nivaa):
    if nivaa < 0:
        return
    turtle.forward(lengde/2)
    turtle.left(30)
    tegn_tre(lengde/1.4, nivaa-1)
    turtle.right(60)
    tegn_tre(lengde/1.4, nivaa-1)
    turtle.left(30)
    turtle.penup()
    turtle.backward(lengde/2)
    turtle.pendown()


if __name__ == "__main__":
    turtle.setup(600,600, 0, 0)
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.speed(10000)
    tegn_tre(300, 3)
    turtle.done()
