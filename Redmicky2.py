import turtle as tur


tur.setup(800,800)
tur.bgcolor("red")
tur.title("Coding with Sadia - Micky")
tur.turtlesize(2,2,2)

tur.setpos(0,-200)

def rel_pos(x,y):
    tur.up()
    tur.goto(tur.pos()+(x,y))
    tur.down()

def go_to(x,y):
    tur.up()    
    tur.goto(x,y)
    tur.down()

def fill_circle(radius,angle=360):
    tur.begin_fill()
    tur.circle(radius,angle)
    tur.end_fill()
    
def draw_oval(width, height, color, x, y, fill=True):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()
    tur.color(color)
    if fill:
        tur.begin_fill()
    for _ in range(2):
        tur.circle(height/2, 45) 
        tur.circle(width/2, 135)
    if fill:
        tur.end_fill() 

def draw_head():
    fill_circle(200)  
    fill_circle(200,135)
    cur_pos = tur.pos() 
    draw_oval(-180,-350,"black",cur_pos[0],cur_pos[1])
    tur.circle(200,90)  
    cur_pos = tur.pos()
    tur.seth(45)
    draw_oval(180,350,"black",cur_pos[0],cur_pos[1])
    tur.seth(125)
    draw_oval(-160,-400,"white",-100,-40)
    tur.seth(55)
    draw_oval(160,400,"white",100,-40)

    tur.seth(160)
    draw_oval(-110,-460,"white",-50,-190)
    tur.seth(20)
    draw_oval(110,460,"white",50,-190)
    tur.seth(-115)
    draw_oval(160,300,"white",-80,-50)

def drawEyes():
    tur.width(8)
    tur.seth(80)
    draw_oval(40,220,"black",-10,0,False)
    tur.left(1)
    draw_oval(10,100,"black",-15,-10)
    tur.seth(90)
    draw_oval(-40,-220,"black",10,0,False)
    tur.right(1)
    draw_oval(-10,-100,"black",15,-10)

def drawNose():
    tur.width(8)
    go_to(-55,-25)
    tur.seth(18)
    tur.circle(-150,40)
    tur.seth(20)
    draw_oval(-50,-110,"black",-20,-35)

def drawMouth():
    tur.seth(-60)
    go_to(-140,-40)
    tur.circle(170,118)

    tur.seth(135)
    tur.circle(20,45)
    tur.seth(10)
    tur.circle(-20,90)

    go_to(-140,-40)
    tur.seth(45)
    tur.circle(-20,45)
    tur.seth(-180)
    tur.circle(20,90)

    tur.begin_fill()
    tur.seth(-65)
    go_to(-140,-40)
    tur.circle(170,30)
    toung_pos = tur.pos()

    tur.seth(-90)
    tur.circle(80,175)
    tur.seth(25)
    tur.circle(170,30)
    tur.seth(-125)
    tur.circle(-170,116)
    tur.end_fill()

    tur.goto(toung_pos)
    tur.fillcolor("red")
    tur.seth(-90)
    tur.circle(80, 40)
    tur.begin_fill()
    tur.circle(80,100)
    tur.seth(135)
    tur.circle(45,80)
    tur.seth(150)
    tur.circle(60,68)
    tur.end_fill()

def drawmicky():
    draw_head()
    drawEyes()
    drawNose()
    drawMouth()

drawmicky()

go_to(-100,-280)
tur.write("""Coding with Sadia\n       Micky""",
          font=("Arial", 20, "bold"))
tur.hideturtle()

tur.done()



          



