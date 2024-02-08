import turtle

size = 200

def pythagoras_tree(n, size):
    if n == 0:
        return
    else:
        turtle.forward(size)
        turtle.right(45)
        pythagoras_tree(n-1, size * 0.7)
        turtle.left(90)
        pythagoras_tree(n-1, size * 0.7)
        turtle.right(45)
        turtle.backward(size)


n = turtle.numinput("Drawing pythagoras tree", "Please enter the number of iterations: ", minval = 0)

turtle.seth(90)
turtle.goto((0, -200))
pythagoras_tree(n, size)

turtle.done()