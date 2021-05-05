import turtle


pen = turtle.Turtle()
 
# function 
def eye(col, rad):
    pen.down()
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()
 
 
# face
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()

#  mouth
pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.up()
 
# eyes
pen.goto(-20, 120)
eye('white', 15)
pen.goto(-30, 120)
eye('black', 5)
pen.goto(40, 120)
eye('white', 15)
pen.goto(30, 120)
eye('black', 5)

turtle.done()
 
 



