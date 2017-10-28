import turtle as t
import random
t.shape ("circle")
t.up()
t.goto(-250,-250)
t.down()
t.speed(0)
def ground(n):
    for x in range(n):
        t.fd(500)
        t.lt(90)

ground(4)
t.up()
t.home()


a=random.randint(0,360)
t.setheading(a)
while -250< t.xcor() <=250  and -250< t.ycor() <=250 :
    t.fd(1)
    
ang = t.heading()
for x in range (500):
    
    if 0< ang < 45 or 135 < ang < 180:
        t.setheading(180-ang)
        t.fd(1)
        while -250<= t.xcor() <=250  and -250<= t.ycor() <=250 :
            t.fd(1)

    if 45< ang <135 or 225 < ang < 315:
        t.setheading(360-ang)
        t.fd(1)
        while -250<= t.xcor() <=250  and -250<= t.ycor() <=250 :
            t.fd(1)

    if 180< ang < 225 or 315 < ang < 360:
        t.setheading(540-ang)
        t.fd(1)
        while -250<= t.xcor() <=250  and -250<= t.ycor() <=250 :
            t.fd(1)

    if ang == 0 or 45 or 90 or 135 or 180 or 225 or 270 or 315 or 360:
        t.lt(180)
        t.fd(1)
        while -250<= t.xcor() <=250  and -250<= t.ycor() <=250 :
            t.fd(1)

