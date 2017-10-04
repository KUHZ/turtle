import turtle

#def draw_square():
def draw():
    window = turtle.Screen()
    window.bgcolor("green")

    count = 0
    t1 = turtle.Turtle()
    t1.shape("turtle")
    t1.color("yellow","red")#yellow is the border,red is inside
    t1.speed(2)
    
    '''
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)   don't use duplicate code
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    '''
    while(count<4):
        t1.forward(100)
        t1.right(90)
        count = count + 1
    
    t2 = turtle.Turtle()
    t2.shape("arrow")
    t2.color("blue")
    t2.speed(2)
    t2.circle(100)

    window.exitonclick()

draw()
