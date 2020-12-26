import turtle

def triangle(lengde, nivaa):
    for i in range(3):
        koch_snowflake(lengde, nivaa)
        turtle.right(120)

def koch_snowflake(lengde, nivaa):
    if nivaa == 0:
        turtle.forward(lengde)
        return
    else:
        koch_snowflake(lengde / 3, nivaa-1)
        turtle.left(60)
        koch_snowflake(lengde / 3, nivaa - 1)
        turtle.right(120)
        koch_snowflake(lengde / 3, nivaa - 1)
        turtle.left(60)
        koch_snowflake(lengde / 3, nivaa - 1)


if __name__ == "__main__":
    turtle.setup(1000, 1000, 0, 0)
    turtle.penup()
    turtle.setpos(-250, 150)
    turtle.pendown()
    turtle.speed(1000)
    triangle(500, 2)
    turtle.done()