import turtle as trtl
from os import path
import tkinter as Tk
import random as rand
import time as t

#shit
key_pen=trtl.Turtle

#setup
score=0
upgrades=0
points=1
fertilizer_cost=2000
plantation_cost = 200
silver_cost = 20
wn = trtl.Screen()
#shapes
wn.register_shape("banana.gif")
clicker = trtl.Turtle()
clicker.shape("banana.gif")
clicker.penup()
clicker.goto(0,-100)


wn.register_shape("smol silver_bannana.gif")
silver_b = trtl.Turtle()
silver_b.shape("smol silver_bannana.gif")
silver_b.penup()
silver_b.goto(-200,200)



wn.register_shape("smol bananana plantation.gif")
plantation = trtl.Turtle()
plantation.shape("smol bananana plantation.gif")
plantation.penup()
plantation.goto(-100,200)


wn.register_shape("Factory-1.gif")
Fact = trtl.Turtle()
Fact.shape("Factory-1.gif")
Fact.penup()
Fact.goto(50,200)


wn.register_shape("smol trans fertilizer.gif")
fert = trtl.Turtle()
fert.shape("smol trans fertilizer.gif")
fert.penup()
fert.goto(150,200)


#setup
font_setup = ("Arial", 40, "normal")
score_pen = trtl.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0,300)

points = 1
upgrade = ["smol bananana plantation.gif","Factory-1.gif"]
purchases=upgrade.pop(upgrades)


#Variables
#Upgrades
def twox_upgrade():
  global points
  global score
  global silver_cost
  if score <= silver_cost:
    print("nothing")
  else:
    points = points*2
    score = score- silver_cost
    silver_cost = silver_cost + 200
    update_score()
    
def fourx_upgrade():
    global points
    global score
    global plantation_cost
    if score <= plantation_cost:
        print("nothing for four")
    else:
        points=points*4
        score=score-plantation_cost
        plantation_cost=plantation_cost+600
        
def eightx_upgrade():
    global points
    global score
    global fertilizer_cost
    if  score<=fertilizer_cost:
        print("nothing for eight")
    else:
        points=points*8
        score=score-fertilizer_cost
        fertilizer_cost=fertilizer_cost*2
        
        
'''def key():
  key_pen.penup()
  key_pen.goto(300,300)
  key_pen.pendown()
  key_pen.write("space is +",points,"bananas")
  key_pen.penup()
  key_pen.goto(100, 150)
  key_pen.write("G is silver bananan upgrade")'''
px = 100
py = 0
def plantation():
  global score
  if score <= plantation_cost:
    print("nothing")
  else:
    activated = trtl.Turtle()
    activated.goto(px,py)
    px - 75
    upgrades + 1 
    score += score + 10*upgrades

def update_score():
    global score
    global upgrades
    upgrades += 1
    score += points
    score_pen.clear()
    (score_pen.write(score,font=font_setup))




wn.onkeypress(update_score, "space")
wn.onkeypress(twox_upgrade, "g")
wn.onkeypress(fourx_upgrade, "h")
wn.onkeypress(eightx_upgrade, "j")


wn.listen()
wn.mainloop()
