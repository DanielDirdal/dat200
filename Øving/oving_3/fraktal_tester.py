import turtle

def triangle(lengde, nivaa):
    for i in range(4):
        koch_snowflake(lengde, nivaa)
        turtle.right(90)

def koch_snowflake(lengde, nivaa):
    if nivaa == 0:
        turtle.forward(lengde)
        return
    else:
        koch_snowflake(lengde / 3, nivaa-1)
        turtle.left(90)
        koch_snowflake(lengde / 3, nivaa - 1)
        turtle.right(90)
        koch_snowflake(lengde / 3, nivaa - 1)
        turtle.right(90)
        koch_snowflake(lengde / 3, nivaa - 1)
        turtle.left(90)
        koch_snowflake(lengde / 3, nivaa - 1)


if __name__ == "__main__":
    turtle.setup(1000, 1000, 0, 0)
    turtle.penup()
    turtle.setpos(-250, 250)
    turtle.pendown()
    turtle.speed(5)
    triangle(500, 2)
    turtle.done()