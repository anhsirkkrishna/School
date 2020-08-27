import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.title('Python')
wn = turtle.Screen()
wn.bgcolor('black')
t.speed(6)

t.pu()
t.goto(-300.90,40.81)
t.pd()
t.dot(25, 'gray')

t.pu()
t.goto(-200, 50)
t.pd()
t.color('gray')
t.begin_fill()
t.fillcolor('gray')
t.rt(45)
t.fd(13)
t.lt(135)
t.fd(200)
t.lt(90)
t.fd(10)
t.lt(90)
t.fd(191)
t.end_fill()
t.goto(-200.81,246.81)
t.begin_fill()
t.lt(90)
t.circle(-60, 180)
t.rt(90)
t.fd(10)
t.rt(90)
t.circle(50, 180)
t.end_fill()
t.color('gray')
t.goto(-190.90,40.81)
t.showturtle()
t.lt(180)
t.pu()
t.fd(100)
t.pd()
t.begin_fill()
t.fd(50)
t.circle(50, 90)
t.fd(150)
t.lt(135)
t.fd(10)
t.lt(45)
t.fd(75)
t.circle(-50, 180)
t.fd(75)
t.lt(45)
t.fd(10)
t.lt(135)
t.fd(80)
t.circle(58, 150)
t.rt(150)
t.fd(35)
t.circle(-50, 90)
t.fd(50)
t.lt(135)
t.fd(10)
t.lt(45)
t.end_fill()


turtle.done()
