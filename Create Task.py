import turtle as trtl
from os import path
import tkinter as Tk
import random as rand
import time as t
#images

wn = trtl.Screen()

score=0


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
wn = trtl.Screen()

font_setup = ("Arial", 40, "normal")
score_pen = trtl.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0,300)

points = 1
upgrades = ["smol bananana plantation.gif","Factory-1.gif"]
banana.pop(upgrades,0)

score = 0
#Variables

def twox_upgrade():
  global points
  global silver_cost
  if score <= silver_cost:
    print("nothing")
  else:
    points = points*2
    score = score- silver_cost
    silver_cost = silver_cost + 200
    update_score()



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


plantation_cost = 200
silver_cost = 20

wn.onkeypress(update_score, "space")
wn.onkeypress(twox_upgrade, "g")

wn.listen()
wn.mainloop()
