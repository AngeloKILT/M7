# Angelo Smith
# 11/16/22
# Question 5 draw a square inside a square and input certain  numbers to find the answer.
import turtle


def draw_square_inside_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")


def spider_squares(z, size):
    alex = turtle.Turtle()
    alex.color("blue")
    size = [30, 60, 90, 120, 180]

    for z in size:
        draw_square_inside_square(alex, z)
        alex.penup()
        alex.backward(20)
        alex.right(90)
        alex.forward(20)
        alex.left(90)
        alex.pendown()


spider_squares(10, 50)
wn.exitonclick()
