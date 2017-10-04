import turtle

#def draw_square():
def draw_square(turtle):
    '''
    window = turtle.Screen()
    window.bgcolor("green")

 
    t1 = turtle.Turtle()
    t1.shape("turtle")
    t1.color("yellow","red")#yellow is the border,red is inside
    t1.speed(2)
    
    
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)   don't use duplicate code
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    '''
    count = 0
    while(count<4):
        turtle.forward(100)
        turtle.right(90)
        count = count + 1

def draw_triangle(turtle):
    count = 0
    while(count<3):
        turtle.forward(100)
        turtle.right(120)
        count = count +1

def draw():
    window = turtle.Screen()
    window.bgcolor("green")
    '''
    #draw square
    t1 = turtle.Turtle()
    t1.shape("turtle")
    t1.color("yellow","red")#yellow is the border,red is inside
    t1.speed(10)
    for i in range(1,73):
         draw_square(t1)
         t1.right(5)
    '''
    #draw circle
    t2 = turtle.Turtle()
    t2.shape("arrow")
    t2.color("blue")
    t2.speed(100)
    radius = 50
    for i in range (1,73):
        t2.circle(radius)
        radius = radius + 1
        t2.right(5)
    
    '''
    #draw triangle
    t3  = turtle.Turtle()
    t3.shape("circle")
    t3.shapesize(0,0,0)
    t3.color("black")
    t3.speed(10)
    for i in range(1,37):
         draw_triangle(t3)
         t3.right(10)
    '''
    

    window.exitonclick()

draw()
