from fltk import *
import random
import os
import sys

h = open('high_score.txt','r')
highscore = h.read()

prev = -100 #called on later, cannot be zero, used for remembering previous values
nums2 = 0
but_shown = []
score = 0
def closewin(widget):
	fl_message('Closing')
	win.hide()
	
def cheat(widget):
	fl_message('''Don't Cheat''')	
	
def res(pic):
	#easy way to resize photos equally so they fit inside the button
	pic = pic.copy(600//4,600//4)
	return(pic)
	
def helpcb(widget):
	#popup that shows instructions.
	fl_message('''Memory Game:
	Objective: Match all pictures, left click to reveal photos among the grid.
	High score is the least attempts to match all of them
	Good Luck! :)
	''')

def but_cb(wid,y):
	#whenever a button is pressed, function is called.
	global but_shown
	global prev
	global files
	global score
	global box1
	global LB
	if prev == y:#gate for errors including the double press of a button
		fl_message('Dont Click a Button Twice')
		
	if prev != y:
		but_shown.append(wid)
		
		if len(but_shown) == 2:#run tests here for the disable
			if files[prev] == files[y]:
				for buttons in but_shown:#detects matches
					buttons.deactivate()
					buttons.redraw()
					but_shown = []
					LB.remove(buttons)
					
													
		if len(but_shown) >= 3:
			for buttons in but_shown:
				buttons.image(res(pic)) #removes shown images when its 3 images
				buttons.redraw()
			but_shown = []
			but_shown.append(wid)
			
			
		if len(LB) == 0:
			fl_message(f'You Won! It took you {score} Amount of Turns')
			if score<=int(highscore):
				outf = open('high_score.txt','w') #win detection
				outf.write(str(score))
				outf.close()
				fl_message('You Got a New Highscore!')
				
				
		prev = y
		score +=1
		box1.label(f'Score: {score}') #box that shows scores
		box1.redraw()

		L = files[y]
		L = res(L)

		wid.image(L)
			
files = []	
temp=['banana.png','dragonfruit.png','kiwi.png','lemon.png','lime.png','orange.png','passionfruit.png','peach.png','pear.png','pineapple.png','rasberry.png','strawberry.png']
for x in temp:
	files.append(Fl_PNG_Image(x))
	
x = 600 #for equal sizes amongst windows and buttons

scramble = (random.sample(range(-12,12),24)) #needs negative and positive indexes for two photos

win = Fl_Window(0,0,x+500,x+100,'Game')
win.begin()

LB = []

G = Fl_Group(0,0,x+300,x)
pic = Fl_PNG_Image('title.png')

box1 = Fl_Box(0,x,x+300,100)
box1.label('Score: 0')

box2 = Fl_Box(x+300,0,175,x+100)
box2.label(f'Current High Score: {highscore}')

menu = Fl_Menu_Bar(0,0,win.w(),25)

menu.add('Exit',FL_F+5,closewin)

menu.add('Help',0,helpcb)

menu.add('Cheat',0,cheat)

for row in range(4):
	for col in range(6):
		count = scramble[nums2]
		LB.append(Fl_Button(col*x//4,(row*x//4)+25,x//4,x//4))
		LB[-1].image(res(pic))
		LB[-1].callback(but_cb,count)		
		nums2+=1
		
G.end()
win.end()
win.show()
Fl.run()
