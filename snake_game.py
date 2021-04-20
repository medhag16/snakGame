#snake game
import turtle
import time
import random

delay=0.2

#setting up a screen
window=turtle.Screen()
window.title("Medha's Snake Game")
window.bgcolor('lightgreen')
window.setup(width=700, height=700)
window.tracer(0) #turns off screen updates

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape('triangle')
head.color('white')
head.penup()
head.goto(0,0)
head.direction='stop'

#food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(random.randrange(-350,350,20),random.randrange(-280,260,20))

snakebod=[]

#to write on screen
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('darkblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('SCORE: 0   HIGH SCORE: 0',align='center', font=('Courier',24,'normal'))

score=0
high_score=0

#move head
def moveup():
    if head.direction!='down':
        head.direction='up'
def moveleft():
    if head.direction!='right':
        head.direction='left'
def moveright():
    if head.direction!='left':
        head.direction='right'
def movedown():
    if head.direction!='up':
        head.direction='down'
def move():
    if head.direction=='up':
        head.sety(head.ycor()+20)

    if head.direction=='down':
        head.sety(head.ycor()-20)

    if head.direction=='left':
        head.setx(head.xcor()-20)

    if head.direction=='right':
        head.setx(head.xcor()+20)

#keyboard input
window.listen()
window.onkeypress(moveup,'Up')
window.onkeypress(movedown,'Down')
window.onkeypress(moveleft,'Left')
window.onkeypress(moveright,'Right')
window.onkeypress(moveup,'w')
window.onkeypress(movedown,'s')
window.onkeypress(moveleft,'a')
window.onkeypress(moveright,'d')
#main game loop
while True:
    window.update()

    #collision border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        delay=0.1
        score=0
        pen.clear()
        pen.write('SCORE %d   HIGH SCORE: %d'%(score, high_score),align='center', font=('Courier',24,'normal'))
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
        for j in snakebod:
            j.hideturtle()
        snakebod.clear()
        
    
    #collision food
    if head.distance(food)<20:
        delay-=0.005
        x=random.randrange(-280,280,20)
        y=random.randrange(-280,260,20)
        food.goto(x,y)
        newbod=turtle.Turtle()
        newbod.speed(0)
        newbod.shape('circle')
        newbod.color('black')
        newbod.penup()
        snakebod.append(newbod)
        score+=5
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write('SCORE %d   HIGH SCORE: %d'%(score, high_score),align='center', font=('Courier',24,'normal'))

    #moving body
    for i in range(len(snakebod)-1,0,-1):
        x=snakebod[i-1].xcor()
        y=snakebod[i-1].ycor()
        snakebod[i].goto(x,y)
    if len(snakebod)>0:
        x=head.xcor()
        y=head.ycor()
        snakebod[0].goto(x,y)
        

    move()

    #collision body
    for bod in snakebod:
        if bod.distance(head)<20:
            delay=0.1
            score=0
            pen.clear()
            pen.write('SCORE %d   HIGH SCORE: %d'%(score, high_score),align='center', font=('Courier',24,'normal'))
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            for j in snakebod:
                j.hideturtle()
            snakebod.clear()
            break
    
    time.sleep(delay)

window.mainloop()
