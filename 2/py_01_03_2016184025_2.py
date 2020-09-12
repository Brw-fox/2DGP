import turtle as t

t.shape("turtle")
t.speed(0)

size = 100
count = 5

x, y = t.pos()

def movepen(x, y):
    t.up()
    t.setpos(x,y)
    t.down()

def draw_line(x,y):
    movepen(x,y)
    t.forward(size * count)

for i in range(count + 1):
    draw_line(x, y)
    y = y + size

y = y - size
t.seth(-90)

for i in range(count + 1):
    draw_line(x, y)
    x = x + size

    
