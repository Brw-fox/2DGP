import turtle as t

t.shape("turtle")
scale = 100

t.colormode(255)
t.pen(pencolor=(77,147,221),pensize = 3, speed = 7)

def movepen(x,y):
	t.up()
	t.setpos(x,y)
	t.down()

def draw_ieung(m = 1):
    t.setheading(0)
    t.circle(scale * 0.5 * m)

def draw_i(m = 1):
	x, y = t.pos()
	movepen(x + scale * 0.8, y + scale * 1.2)
	t.seth(-90)
	t.forward(scale * 1.5 * m)
	movepen(x, y)

def draw_ya(m=1):
    draw_i(m)
    x, y = t.pos()
    t.seth(0)
    for i in range(1,3):
    	movepen(x + scale * 0.8, (y + scale * 1.2) - i * (scale // 2 *m))
    	t.forward(scale // 2 * m)
    movepen(x, y)

def draw_mieum(m = 1):
	x,y= t.pos()
	t.seth(90)
	movepen(x + scale / 2 * m, y)
	for i in range(1,5):
		t.forward(scale * m)
		t.left(90)
	movepen(x,y)

def draw_nien(m = 1):
	x, y = t.pos()
	movepen(x - scale / 2 * m, y + scale * m)
	t.seth(-90)
	t.forward(scale * m)
	t.left(90)
	t.forward(scale * m)
	movepen(x,y)

def draw_siot(m = 1):
	x , y = t.pos()
	movepen(x, y + scale * m)
	t.seth(-120)
	t.forward(scale * m)
	t.backward(scale // 2 * m)
	t.left(60)
	t.forward(scale // 2 * m)
	movepen(x,y)


def draw_eu(m = 1):
	x, y = t.pos()
	t.seth(0)
	movepen(x - scale * 0.7 * m, y - scale * 0.3 * m)
	t.forward(scale * 1.5 * m)
	movepen(x,y)

def draw_u(m=1):
	draw_eu()
	x, y = t.pos()
	t.seth(-90)
	movepen(x, y - scale * 0.3 * m)
	t.forward(scale / 2 * m)
	movepen(x,y)

def draw_final(func = None):
	x, y = t.pos()
	if(func != None):
		movepen(x, y - scale * 1.5)
		func()
	movepen(x + scale * 2.5, y)

movepen(-250,0)
draw_ieung()
draw_ya()
draw_final(draw_ieung)

draw_siot()
draw_i()
draw_final()

draw_mieum()
draw_u()
draw_final(draw_nien)

t.exitonclick()

