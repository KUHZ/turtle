import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")

    t1 = turtle.Turtle()
    t1.shape("turtle")
    t1.color("yellow","red")
    t1.speed(2)
    
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)

    window.exitonclick()

draw_square()
