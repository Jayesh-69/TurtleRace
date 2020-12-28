import turtle
import random
import os

colo = ['red','yellow','black','green','blue','orange','violet','purple']
noOfTurtle = 8
t = []

# Making Finish line
fl = turtle.Turtle()
fl.penup()
fl.setpos(140,150)
fl.pendown()
fl.setheading(180)
fl.forward(320)
fl.penup()
fl.forward(500)  # making disapear the arrow

x = -150
for i in range(noOfTurtle):
    t.append(turtle.Turtle())
    t[i].shape('turtle')
    t[i].color(colo[i])
    t[i].penup()
    t[i].goto(x,-200)
    t[i].write(colo[i],False,align = 'center')
    x += 40
    t[i].setheading(90)
    t[i].forward(20)
    t[i].pendown()

flag = True
while flag:
    for i in range(noOfTurtle):
        t[i].forward(random.randint(0,25))
        x,y = t[i].pos()
        if y > 150 :
            winner = colo[i]
            flag = False

print("Winner is ==> " +winner)

def setScores():
    oldScore = []
    with open('scores.txt','r') as scr:
        for line in scr:
            l = line.split()
            colorr = l[0]
            score = l[1]
            oldScore.append([colorr, score])

    with open('scores.txt','w') as scr:
        for entry in oldScore:
            if entry[0] == winner:
                entry[1] = int(entry[1])+1
            scr.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')

setScores()

turtle.done()