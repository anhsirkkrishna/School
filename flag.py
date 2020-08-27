import turtle

t = turtle.Turtle()
wn = turtle.Screen()

t.speed(0)

wn.bgcolor('black')
wn.title('Flag')

t.hideturtle()
t.showturtle()
t.begin_fill()
turtle.colormode(255)
t.color(139,69,19)

t.fd(10)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(10)
t.lt(90)
t.fd(300)
t.end_fill()

t.goto(10, 300)

t.color(255,119,51)
t.begin_fill()
t.lt(90)
t.fd(150)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(50)
t.end_fill()

t.lt(180)
t.fd(50)

t.begin_fill()
t.color('white')

t.fd(50)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(150)
t.end_fill()

t.goto(10,200)

t.color('green')

t.goto(10, 150)

t.begin_fill()
t.rt(180)
t.fd(150)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(150)
t.end_fill()

t.bk(75)
t.color('blue')
t.circle(-25)

t.rt(90)
t.fd(50)
t.rt(90)
t.circle(-25, 90)
t.rt(90)
t.fd(50)

t.rt(90)
t.circle(-25, 45)
t.rt(90)
t.fd(50)

t.rt(90)
t.circle(-25, 90)
t.rt(90)
t.fd(50)
t.lt(135)


t.pu()
t.goto(0, 0)
t.pd()

t.color(139,69,19)

t.fd(100)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(210)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(100)

t.pu()
t.goto(-100, -30)
t.showturtle()

t.pd()
t.fd(30)
t.lt(90)
t.fd(50)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(50)
t.rt(90)
t.bk(330)

t.rt(90)
t.fd(50)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(240)

t.goto(-100, 0)

t.rt(135)
t.fd(25)
t.rt(45)
t.fd(222)
t.rt(90)
t.fd(49)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.rt(45)
t.fd(60)

turtle.done()