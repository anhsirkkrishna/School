import turtle

t = turtle.Turtle()

t.hideturtle()

t.speed(0)

wn = turtle.Screen()
turtle.title('Circles')
wn.bgcolor('black')

for i in range(6):
	for color in ['blue', 'green', 'cyan', 'pink', 'yellow', 'red']:
		t.color(color)
		t.circle(100)
		t.lt(10)

turtle.done()