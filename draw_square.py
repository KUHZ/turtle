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
        turtle.forward(50)
        turtle.right(120)
        count = count +1

def draw():
    window = turtle.Screen()
    window.bgcolor("green")
    #draw square
    t1 = turtle.Turtle()
    t1.shape("turtle")
    t1.color("yellow","red")#yellow is the border,red is inside
    t1.speed(2)
    draw_square(t1)
    #draw circle
    t2 = turtle.Turtle()
    t2.shape("arrow")
    t2.color("blue")
    t2.speed(2)
    t2.circle(100)
    #draw triangle
    t3  = turtle.Turtle()
    t3.shape("arrow")
    t3.color("black")
    draw_triangle(t3)
 
    

    window.exitonclick()

draw()
