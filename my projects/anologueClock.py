#  analogue clock
import turtle
import datetime
import time
#  screen leveling
window_screen=turtle.Screen()
window_screen.tracer(0)
window_screen.bgcolor("black")
#declaring the turtles 
writer=turtle.Turtle()
writer.hideturtle()
second_hand=turtle.Turtle()
second_hand.hideturtle()
minute_hand=turtle.Turtle()
minute_hand.hideturtle()
hour_hand=turtle.Turtle()
hour_hand.hideturtle()
#  read the current time
hour =datetime.datetime.now().hour
minute =datetime.datetime.now().minute
second=datetime.datetime.now().second
#  structure of the whole clock
def structure(): 
    writer.lt(90)
    hyphen_number=60
    while hyphen_number >= 1:
        if hyphen_number%5 == 0:
            writer.color("brown")
            writer.penup()
            writer.fd(200)
            writer.pendown()
            writer.pensize(7)
            writer.fd(20)
            writer.penup()
            writer.bk(220)
            writer.penup()
        else:
            writer.color("white")
            writer.penup()
            writer.fd(200)
            writer.pendown()
            writer.pensize(3)
            writer.fd(10)
            writer.penup()
            writer.bk(210)
            writer.penup()
        writer.right(6)
        hyphen_number = hyphen_number - 1 
    clock_number = 1
    while clock_number <= 12:
        writer.right(30)
        writer.penup()
        writer.fd(150)
        writer.pendown()
        writer.color("white")
        writer.write(str(clock_number),align='center',font=('Times New Roman',16,'normal'))
        writer.penup()
        writer.bk(150)
        writer.pendown()
        clock_number= clock_number + 1
        writer.hideturtle()
    hour_hand.pensize(5)
    hour_hand.color("white")
    hour_hand.rt(90 + (hour + minute/60 + second/3600)*30)
    hour_hand.pensize(3)
    hour_hand.fd(65)

    minute_hand.color("white")
    minute_hand.pensize(1.8)
    minute_hand.lt(90)
    minute_hand.rt((minute + second/60)*6)
    minute_hand.fd(100)

    second_hand.hideturtle()
    second_hand.color("white")
    second_hand.pensize(1.4)
    second_hand.lt(90)
    second_hand.rt(second*6)
# functions of movement    
def hour_move():
    hour_hand.penup()
    hour_hand.goto(0,0)
    hour_hand.rt(1/120)
    hour_hand.pendown()
    hour_hand.fd(65)
structure()
def minute_move():
    minute_hand.penup()
    minute_hand.goto(0,0)
    minute_hand.rt(1/10)
    minute_hand.pendown() 
    minute_hand.fd(100)
def second_move():
    second_hand.fd(120)
    second_hand.penup()
    second_hand.goto(0,0)
    second_hand.rt(6)
    second_hand.pendown() 
# infinite loop  

while True :
    second_move()
    minute_move()
    hour_move()
    window_screen.update()
    second_hand.clear()
    minute_hand.clear()
    hour_hand.clear()
    time.sleep(1)
turtle.done()