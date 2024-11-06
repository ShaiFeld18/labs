import turtle
import turtle as tr


def draw_triangle():
    """This function draws a triangle"""
    tr.forward(45)
    tr.right(120)
    tr.forward(45)
    tr.right(120)
    tr.forward(45)
    tr.right(120)


def draw_sail():
    """This function draws a sail"""
    tr.left(90)
    tr.forward(50)
    tr.right(150)
    draw_triangle()
    tr.right(30)
    tr.up()
    tr.forward(50)
    tr.down()
    tr.left(90)


def draw_ship():
    """This function draws a ship"""
    tr.right(90)
    tr.forward(50)
    for i in range(3):
        draw_sail()
        tr.forward(50)
    tr.right(120)
    tr.forward(20)
    tr.right(60)
    tr.forward(180)
    tr.right(60)
    tr.forward(20)
    tr.right(30)


def draw_fleet():
    # turn turtle to required direction
    tr.left(90)

    # draw first ship
    draw_ship()

    # move turtle to next ship's position
    tr.up()
    tr.left(90)
    tr.forward(300)
    tr.right(90)
    tr.down()

    # draw second ship
    draw_ship()

    # return to original position
    tr.up()
    tr.right(90)
    tr.forward(300)
    tr.left(90)


if __name__ == '__main__':
    draw_fleet()
    turtle.done()
