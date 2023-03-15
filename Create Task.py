import turtle as trtl
import tkinter as Tk
import random as rand
import time as t
from PIL import Image
#images
'''clicker = "banana.gif"'''
'''clicker = Image.open('banana.gif')
new_image = clicker.resize((400, 400))
Image._show(clicker)'''


with Image.open("banana.gif") as im:
    im.rotate(45).show()


jungle = "jungle.gif"
silver_banana = "silver_banana.gif"
plantation = "banana plantation.gif"
factory = "banana factory.gif"
bank = "USAa Bank.gif"


#setup
wn = trtl.Screen()
wn.bgcolor('gray')

font_setup = ("Arial", 20, "normal")
score_pen = trtl.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0,300)

#Variables
'''def draw_banana(activate_banana):
  activate_banana.shape(clicker)
  wn.update()'''

banana = trtl.Turtle()

def update_score():
    global score
    score += 1 
    score_pen.clear()
    (score_pen.write(score,font=font_setup))

def banana_click():
  update_score()








wn.listen()
wn.mainloop()
