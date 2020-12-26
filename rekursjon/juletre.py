import turtle


# Eksempel på en fraktal: Juletre
farger = ["brown", "dark green", "light green", "yellow", "white"]
pennbredder = [4, 2, 1, 1, 1]

def tegn_stjerne(radius):
    for i in range(36):
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.right(10)


def juletre(distanse, nivaa):
    if distanse < 6:
        return
    turtle.pendown()
    if nivaa < len(farger):
        turtle.pencolor(farger[nivaa])
        turtle.pensize(pennbredder[nivaa])
    else:
        turtle.pencolor("white")
        turtle.pensize(1)
    tegn_stjerne(distanse/2)
    turtle.penup()
    turtle.forward(distanse)
    juletre(distanse/2, nivaa+1)
    turtle.backward(distanse)
    turtle.right(120)
    turtle.forward(distanse)
    juletre(distanse/2, nivaa+1)
    turtle.backward(distanse)
    turtle.right(120)
    turtle.forward(distanse)
    juletre(distanse/2, nivaa+1)
    turtle.backward(distanse)
    turtle.right(120)


if __name__ == "__main__":
    turtle.setup(600,600, 0, 0)
    turtle.bgcolor("black")
    turtle.left(90)
    turtle.speed(5)
    juletre(150, 0)
    turtle.done()
