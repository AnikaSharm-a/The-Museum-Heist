#################################
# Title: The Museum Heist
# Programmer: Anika Sharma
# Date: Jan 25, 2022
# Objective: Collect all items and make it to the exit without getting caught by the guards.
#################################








########### IMPORTS + SETUP ##############

from tkinter import *
from time import sleep
from math import sqrt
root = Tk()
s = Canvas(root, width = 800, height = 500, background = "#edcc94")








############## HOW TO PLAY SCREEN ##############

# Home button on "How To Play" screen
def back():
	s.delete("all")
	backb.destroy()
	intro()




# Arrow keys drawing in "How To Play" screen
def createarrowkeys():
	s.create_image(135,125, image = arrows)




# Guard in "How To Play" screen 
def createinfoguard():
	x = 75
	y = 350
	
	# Heads
	s.create_oval(x,y, x+45, y+45, fill = "white")

	# Cap
	s.create_arc(x, y, x+45, y+35, start = 0, extent = 180, fill = "navy")
	s.create_oval(x+25,y+5, x+60,y+17, fill = "navy", outline = "")

	# eyes
	s.create_oval(x+30, y+20, x+35,y+30, fill = "black")

	# moustache
	s.create_oval(x+45,y+30, x+21,y+35, fill = "brown", outline = "")

	# mouth
	s.create_line(x+37,y+38, x+26,y+38, width = 2)

	# Light
	s.create_polygon(x+45+18,y+26, x+45+74,y+9, x+45+74,y+45, fill = "yellow")

	# Flashlight body
	s.create_polygon(x+45+18,y+26, x+45+36,y+20, x+45+36,y+34, fill = "grey", outline = "black")
	s.create_rectangle(x+45+3,y+23,x+45+26,y+30, fill = "grey")




# Lives box in "How To Play" screen
def drawInfoLives():
	s.create_rectangle(77,415, 193,460, fill = "palegreen2", outline = "slateblue1", width = 2)
	s.create_text(135,435, text = "Lives: 3", font = "Times 15")




# Diamond image in "How To Play" screen
def createDiamond():
	s.create_image(137,250, image = d)




# How To Play screen
def instructions():
	global backb, arrows, d

	# Destroying + deleting everything from homescreen
	bl1.destroy()
	bl2.destroy()
	bl3.destroy()
	ibutton.destroy()
	s.delete("all")


	# Background
	x = 0
	for i in range(50):
		s.create_rectangle(x,0, x+20,500, fill = "#e0bc82", outline = "")
		x += 40 


	# Header with title
	s.create_rectangle(0,0, 805,60, fill = "lightsteelblue", outline = "slateblue", width = 2)
	s.create_text(400,30, text = "How To Play", font = "Times 25")


	# Home button
	backb = Button(text = "Home", font = "Times 10", command = back)
	backb.place(x = 675, y = 15, width = 75, height = 30)

	
	# Arrow keys drawing + instruction
	arrows = PhotoImage(file = "arrow keys.png")
	createarrowkeys()
	s.create_text(375,140, text = "Arrow keys to move the player:", font = "Times 15")


	# Player drawing 
	xval = 550
	yval = 100

	# Face
	s.create_oval(xval,yval, xval+45, yval+45, fill = "white")
	s.create_arc(xval,yval, xval+45, yval+35, start = 0, extent = 180, fill = "black")
	s.create_arc(xval,yval+8, xval+45,yval+45, start = 0, extent = -180, fill = "black")
	
	# Eyes
	s.create_oval(xval+13,yval+27, xval+18,yval+22, fill = "black")
	s.create_oval(xval+28,yval+27, xval+33,yval+22, fill = "black")

	s.create_text(573,155, text = "(you)", font = "times 10")


	# "p" button drawing + instruction
	s.create_rectangle(115,175, 155,215, fill = "black")
	s.create_text(135,195, text = "p", font = "arial 20", fill = "white")
	s.create_text(400,200, text = "Press p on top of an item to collect it", font = "times 15")


	# Item drawing + instruction
	d = PhotoImage(file = "tkinter diamond.png")
	createDiamond()
	s.create_text(403,250, text = "Collect all items in the museum room", font = "times 15")


	# Exit door drawing + instruction
	s.create_rectangle(75,285, 195,335, fill = "lemonchiffon2", outline = 'brown', width = 3)
	s.create_line(137,285, 137,335, fill = "brown", width = 10)
	s.create_text(440,310, text = "Make it to this exit door with all items to win", font = "Times 15")


	# Guard drawing + instruction
	createinfoguard()
	s.create_text(477,375, text = "Don't get caught by the guards and their flashlights", font = "Times 15")


	# Lives drawing + instruction
	drawInfoLives()
	s.create_text(460,438, text = "You lose a life when you get caught. You have 3 \nlives per level", font = "Times 15")








############## HOMESCREEN ##############

# Level one initiation from homescreen 
def l1():
	global level
	level = 1

	bl1.destroy()
	bl2.destroy()
	bl3.destroy()
	ibutton.destroy()
	s.delete("all")
	
	runGame()




# Level two initiation from homescreen 
def l2():
	global level
	level = 2

	bl1.destroy()
	bl2.destroy()
	bl3.destroy()
	ibutton.destroy()
	s.delete("all")
	
	runGame()




# Level three initiation from homescreen 
def l3():
	global level
	level = 3

	bl1.destroy()
	bl2.destroy()
	bl3.destroy()
	ibutton.destroy()
	s.delete("all")
	
	runGame()




# Creating images on homescreen
def createImages():
	s.create_image(400,100, image = textfile)
	s.create_image(525,265, image = introdiamondfile)
	s.create_image(275,265, image = playerfile)




# Homescreen
def intro(): 
	global textfile, introdiamondfile, playerfile, bl1, bl2, bl3, ibutton


	# floor
	x = 0
	for i in range(50):
		s.create_rectangle(x,0, x+20,500, fill = "#e0bc82", outline = "")
		x += 40 

	# carpet
	s.create_rectangle(0,225, 805,325, fill = "orangered", outline = "")
	s.create_line(0,240, 805,240, fill = "gold", width = 2)
	s.create_line(0,310, 805,310, fill = "gold", width = 2)


	# title box
	s.create_rectangle(125,50, 675,150, fill = "#e9f5f9", outline = "#3ba1c5", width = 10)
	textfile = PhotoImage(file = "text.png")	


	# Diamond, player and title images
	introdiamondfile = PhotoImage(file = "intro diamond.png")
	playerfile = PhotoImage(file = "intro player.png")
	createImages()


	# Level 1 button
	bl1 = Button(root, bg = "palegreen3", activebackground = "palegreen1", text = "Level 1", font = "Times 15", command = l1)
	bl1.place(x = 125, y = 350, width = 150, height = 50)

	# Level 2 button
	bl2 = Button(root, bg = "palegreen3", activebackground = "palegreen1", text = "Level 2", font = "Times 15", command = l2)
	bl2.place(x = 325, y = 350, width = 150, height = 50)

	# Level 3 button
	bl3 = Button(root, bg = "palegreen3", activebackground = "palegreen1", text = "Level 3", font = "Times 15", command = l3)
	bl3.place(x = 525, y = 350, width = 150, height = 50)

	# How To Play button
	ibutton = Button(root, bg = "lightskyblue", activebackground = "lightskyblue1", text = "How To Play", font = "Times 15", command = instructions)
	ibutton.place(x = 300, y = 425, width = 200, height = 50)








############## INITIAL VALUES ##############

# Initial values for the game
def setInitialvalues():
	global xval, yval, xspeed, yspeed, lives, itemscollected, pdirection, won, pquit
	global numGuards, xguards, yguards, gxspeeds, gyspeeds, guards, gdirections
	global gheads, gcaps, gcaps2, geyesL, geyesR, gMsL, gMsR, gmouths, bodyf, bodyf2, light
	global doorx, doory, totalitems
	global xcheese, ycheese, cheesefile, cheesedeleted 
	global xshirt, yshirt, shirtfile, shirtdeleted
	global xshoe, yshoe, shoefile, shoedeleted
	global xpurse, ypurse, pursefile, pursedeleted
	global xpainting, ypainting, paintingfile, paintingdeleted
	global xdiamond, ydiamond, diamondfile, diamonddeleted


	# Player
	xval = 25
	yval = 250
	pdirection = "down"
	xspeed = 0
	yspeed = 0
	lives = 3
	won = False
	itemscollected = 0
	pquit = False


	###### LEVEL 1 #######
	if level == 1:
		# Exit
		doorx = 750
		doory = 200

		# Items 
		totalitems = 1 
		xcheese = 400
		ycheese = 275
		cheesefile = PhotoImage(file = "tkinter cheese.png")
		cheesedeleted = False

		# Guards 
		numGuards = 2
		xguards = [230, 520]
		yguards = [131, 384]
		gdirections = ["down", "up"]
		gxspeeds = [0, 0]
		gyspeeds = [3, -3]


	###### LEVEL 2 #######
	if level == 2:
		# Exit
		doorx = 600
		doory = 450

		# Items 
		totalitems = 2
		
		xshirt = 700
		yshirt = 100
		shirtfile = PhotoImage(file = "tkinter shirt.png")
		shirtdeleted = False

		xshoe = 100
		yshoe = 450
		shoefile = PhotoImage(file = "tkinter shoe.png")
		shoedeleted = False

		# Guards 
		numGuards = 3
		xguards = [100, 625, 400]
		yguards = [131, 384, 384]
		gdirections = ["right", "left", "up"]
		gxspeeds = [3, -3, 0]
		gyspeeds = [0, 0, -3]


	###### LEVEL 3 ######## 
	if level == 3:
		# Exit
		doorx = 200
		doory = 55

		# Items 
		totalitems = 3
		
		xpurse = 600
		ypurse = 125
		pursefile = PhotoImage(file = "tkinter purse.png")
		pursedeleted = False

		xpainting = 275
		ypainting = 275
		paintingfile = PhotoImage(file = "tkinter painting.png")
		paintingdeleted = False

		xdiamond = 650
		ydiamond = 450
		diamondfile = PhotoImage(file = "tkinter diamond.png")
		diamonddeleted = False

		# Guards 
		numGuards = 4
		xguards = [125, 375, 500, 750]
		yguards = [131, 384, 131, 375]
		gdirections = ["down", "up", "down", "left"]
		gxspeeds = [0, 0, 0, -3]
		gyspeeds = [3, -3, 3, 0]


	# Guard arrays 
	gheads = []
	gcaps = []
	gcaps2 = []
	geyesL = []
	geyesR = []
	gMsL = []
	gMsR = []
	gmouths = []
	bodyf = []
	bodyf2 = []
	light = []

	# Filling guard arrays
	for i in range(numGuards):
		gheads.append(0)
		gcaps.append(0)
		gcaps2.append(0)
		geyesL.append(0)
		geyesR.append(0)
		gMsL.append(0)
		gMsR.append(0)
		gmouths.append(0)
		bodyf.append(0)
		bodyf2.append(0)
		light.append(0)








############### DRAWING ###############

# Background
def drawBackground():
	global qbutton

	# floor
	x = 0
	for i in range(50):
		s.create_rectangle(x,0, x+20,500, fill = "#e0bc82", outline = "")
		x += 40 

	# carpet
	s.create_oval(400-150,280-150, 400+150,280+150, fill = "orangered", outline = "")
	s.create_oval(400-100,280-100, 400+100,280+100, fill = "", outline = "gold", width = 3)


	# quit button
	qbutton = Button(text = "Quit", font = "Times 10", command = quit)
	qbutton.place(x = 20, y = 20, width = 60, height = 30)


	# DOOR #

	if level == 1:
		s.create_rectangle(doorx,doory, doorx+55,doory+145, fill = "lemonchiffon2", outline = 'brown', width = 3)
		s.create_line(doorx,doory+72, doorx+55,doory+72, fill = "brown", width = 10)

	elif level == 2:
		s.create_rectangle(doorx,doory, doorx+145,doory+55, fill = "lemonchiffon2", outline = 'brown', width = 3)
		s.create_line(doorx+77,doory, doorx+77,doory+50, fill = "brown", width = 10)

	elif level == 3:
		s.create_rectangle(doorx,doory, doorx+145,doory+55, fill = "lemonchiffon2", outline = 'brown', width = 3)
		s.create_line(doorx+75,doory, doorx+75,doory+55, fill = "brown", width = 10)




# Header with all information
def drawHeader():
	global header, livestext, ltext, livesr, itemstext, hcheese, hshirt, hshoe, hpurse, hpainting, hdiamond

	header = s.create_rectangle(0,0, 805,60, fill = "lightsteelblue", outline = "slateblue", width = 2)


	# Level text
	if level == 1: leveltext = "LEVEL 1"
	elif level == 2: leveltext = "LEVEL 2"
	elif level == 3: leveltext = "LEVEL 3"

	ltext = s.create_text(185,30, text = leveltext, font = "times 23")


	# Lives text
	if lives == 3: col = "palegreen2"
	elif lives == 2: col = "yellow2"
	else: col = "tomato2"

	livesr = s.create_rectangle(275,0, 395,59, fill = col, outline = "")
	text = "Lives: " + str(lives)
	livestext = s.create_text(335,30, text = text, font = "Times 15")


	# Items left text
	itemstext = s.create_text(475,30, text= "Items left:", font = "times 15")

	# Level one items
	if level == 1 and not cheesedeleted:
		hcheese = s.create_image(xcheese+175, ycheese-245, image = cheesefile)

	# Level two items
	if level == 2 and not shirtdeleted:
		hshirt = s.create_image(xshirt-125, yshirt-70, image = shirtfile)
	if level == 2 and not shoedeleted:
		hshoe = s.create_image(xshoe+550, yshoe-420, image = shoefile)

	# Level three items
	if level == 3 and not pursedeleted: 
		hpurse = s.create_image(xpurse-25, ypurse-97, image = pursefile)
	if level == 3 and not paintingdeleted:
		hpainting = s.create_image(xpainting+375, ypainting-245, image = paintingfile)
	if level == 3 and not diamonddeleted: 
		hdiamond = s.create_image(xdiamond+85, ydiamond-423, image = diamondfile)


	# Divisions between header sections
	s.create_line(95,0, 95,60, fill = "slateblue", width = 10)
	s.create_line(270,0, 270,60, fill = "slateblue", width = 10)
	s.create_line(400,0, 400,60, fill = "slateblue", width = 10)




# Drawing the items in the level
def drawItems():
	global cheese, shirt, shoe, purse, painting, diamond, platform, platform1, platform2


	# Level 1
	if level == 1:
		platform = s.create_oval(xcheese-40,ycheese-30, xcheese+35,ycheese+30, fill = "gold3", outline = "gold2")
		cheese = s.create_image(xcheese, ycheese, image = cheesefile)


	# Level 2
	elif level == 2:
		platform = s.create_oval(xshirt-40,yshirt-30, xshirt+35,yshirt+30, fill = "gold3", outline = "gold2")
		shirt = s.create_image(xshirt, yshirt, image = shirtfile)

		platform1 = s.create_oval(xshoe-40,yshoe-30, xshoe+35,yshoe+30, fill = "gold3", outline = "gold2")
		shoe = s.create_image(xshoe, yshoe, image = shoefile)


	# Level 3
	elif level == 3:
		platform = s.create_oval(xpurse-40,ypurse-30, xpurse+35,ypurse+30, fill = "gold3", outline = "gold2")
		purse = s.create_image(xpurse, ypurse, image = pursefile)

		platform1 = s.create_oval(xpainting-40,ypainting-30, xpainting+35,ypainting+30, fill = "gold3", outline = "gold2")
		painting = s.create_image(xpainting, ypainting, image = paintingfile)

		platform2 = s.create_oval(xdiamond-40,ydiamond-30, xdiamond+35,ydiamond+30, fill = "gold3", outline = "gold2")
		diamond = s.create_image(xdiamond, ydiamond, image = diamondfile)




# Drawing the player in the game
def drawPlayer():
	global head, mask1, mask2, eye1, eye2

	head = s.create_oval(xval,yval, xval+35, yval+35, fill = "white")


	# If moving down
	if pdirection == "down":
		mask1 = s.create_arc(xval,yval, xval+35, yval+25, start = 0, extent = 180, fill = "black")
		mask2 = s.create_arc(xval,yval+8, xval+35,yval+35, start = 0, extent = -180, fill = "black")

		eye1 = s.create_oval(xval+10,yval+17, xval+15,yval+22, fill = "black")
		eye2 = s.create_oval(xval+20,yval+17, xval+25,yval+22, fill = "black")


	# If moving left
	elif pdirection == "left":
		mask1 = s.create_arc(xval,yval, xval+35,yval+35, start = 160, extent = -330, fill = "black")
	
		eye1 = s.create_oval(xval+3, yval+15, xval+6, yval+20, fill = "black")


	# If moving right
	elif pdirection == "right":
		mask1 = s.create_arc(xval,yval, xval+35,yval+35, start = 17, extent = 330, fill = "black")

		eye1 = s.create_oval(xval+33, yval+15, xval+30, yval+20, fill = "black")
	

	# If moving up
	elif pdirection == "up":
		mask1 = s.create_arc(xval,yval, xval+35,yval+35, start = 0, extent = 359, fill = "black")




# Drawing the guards in the game
def drawGuards():
	for i in range(numGuards):

		x = xguards[i]
		y = yguards[i]

		# Heads
		gheads[i] = s.create_oval(x,y, x+45, y+45, fill = "white")

		# Cap
		gcaps[i] = s.create_arc(x, y, x+45, y+35, start = 0, extent = 180, fill = "navy")


		# If moving up
		if gdirections[i] == "up": 
			
			# FlashLight
			light[i] = s.create_polygon(x+21,y-17, x+5,y-70, x+41,y-70, fill = "yellow")
			bodyf[i] = s.create_polygon(x+21,y-17, x+15,y-35, x+29,y-35, fill = "grey", outline = "black")
			bodyf2[i] = s.create_rectangle(x+18,y-25,x+25,y-2, fill = "grey")
	

		# If moving down
		elif gdirections[i] == "down": 

			# eyes
			geyesL[i] = s.create_oval(x+10, y+20, x+15, y+30, fill = "black")
			geyesR[i] = s.create_oval(x+25, y+20, x+30, y+30, fill = "black")

			# Moustache
			gMsL[i] = s.create_oval(x+5,y+30, x+22, y+35, fill = "brown", outline = "")
			gMsR[i] = s.create_oval(x+20,y+30, x+38, y+35, fill = "brown", outline = "")

			# Mouth
			gmouths[i] = s.create_line(x+16,y+38, x+27,y+38, width = 2)	

			# Flashlight
			light[i] = s.create_polygon(x+21,y+62, x+5,y+115, x+41,y+115, fill = "yellow")
			bodyf[i] = s.create_polygon(x+21,y+62, x+15,y+80, x+29,y+80, fill = "grey", outline = "black")
			bodyf2[i] = s.create_rectangle(x+18,y+70,x+25,y+47, fill = "grey")


		# If moving left
		elif gdirections[i] == "left": 
			
			# cap
			gcaps2[i] = s.create_oval(x-15,y+5, x+20,y+17, fill = "navy", outline = "")

			# eyes
			geyesR[i] = s.create_oval(x+10, y+20, x+15,y+30, fill = "black")

			# moustache
			gMsR[i] = s.create_oval(x,y+30, x+24,y+35, fill = "brown", outline = "")

			# mouth
			gmouths[i] = s.create_line(x+8,y+38, x+15,y+38, width = 2)

			# Flashlight
			light[i] = s.create_polygon(x-18,y+26, x-74,y+9, x-74,y+45, fill = "yellow")
			bodyf[i] = s.create_polygon(x-18,y+26, x-36,y+20, x-36,y+34, fill = "grey", outline = "black")
			bodyf2[i] = s.create_rectangle(x-3,y+23,x-26,y+30, fill = "grey")


		# If moving right
		elif gdirections[i] == "right": 

			# cap
			gcaps2[i] = s.create_oval(x+25,y+5, x+60,y+17, fill = "navy", outline = "")

			# eyes
			geyesR[i] = s.create_oval(x+30, y+20, x+35,y+30, fill = "black")

			# moustache
			gMsR[i] = s.create_oval(x+45,y+30, x+21,y+35, fill = "brown", outline = "")

			# mouth
			gmouths[i] = s.create_line(x+37,y+38, x+26,y+38, width = 2)

			# Flashlight
			light[i] = s.create_polygon(x+45+18,y+26, x+45+74,y+9, x+45+74,y+45, fill = "yellow")
			bodyf[i] = s.create_polygon(x+45+18,y+26, x+45+36,y+20, x+45+36,y+34, fill = "grey", outline = "black")
			bodyf2[i] = s.create_rectangle(x+45+3,y+23,x+45+26,y+30, fill = "grey")








############ UPDATING ###############

# Player updating
def updateplayer():
	global xval, yval

	xval += xspeed
	yval += yspeed




# Guards updating
def updateguards():
	for i in range(numGuards):

		# Down 
		if yguards[i] <= 130: 
			gyspeeds[i] = 3
			gxspeeds[i] = 0
			gdirections[i] = "down"

		# Up
		if yguards[i] >= 385: 
			gyspeeds[i] = -3
			gxspeeds[i] = 0
			gdirections[i] = "up"

		# Right
		if xguards[i] <= 75:
			gyspeeds[i] = 0
			gxspeeds[i] = 3
			gdirections[i] = "right"

		# Left
		if xguards[i] >= 670:
			gyspeeds[i] = 0
			gxspeeds[i] = -3
			gdirections[i] = "left"


		xguards[i] += gxspeeds[i]
		yguards[i] += gyspeeds[i]








########### GAME FUNCTIONALITY ############

# Quit button during gameplay
def quit(): 
	global pquit
	pquit = True




# Checking to see if player is on the item
def checkItem():
	global itemscollected, cheesedeleted, shirtdeleted, shoedeleted, pursedeleted, paintingdeleted, diamonddeleted
	
	# Level 1: cheese
	if level == 1:

		if (xcheese-40 < xval < xcheese+35 or xcheese-40 <= xval+35 <= xcheese+35) and ycheese-30 < yval < ycheese+30 and not cheesedeleted:
			s.delete(cheese) 
			itemscollected += 1
			cheesedeleted = True


	# Level 2: shirt, shoe
	elif level == 2:

		if (xshirt-40 < xval < xshirt+35 or xshirt-40 <= xval+35 <= xshirt+35) and yshirt-30 < yval < yshirt+30 and not shirtdeleted:
			s.delete(shirt) 
			itemscollected += 1
			shirtdeleted = True

		if (xshoe-40 < xval < xshoe+35 or xshoe-40 <= xval+35 <= xshoe+35) and yshoe-30 < yval < yshoe+30 and not shoedeleted:
			s.delete(shoe) 
			itemscollected += 1
			shoedeleted = True


	# Level 3: purse, painting, diamond
	elif level == 3:

		if (xpurse-40 < xval < xpurse+35 or xpurse-40 <= xval+35 <= xpurse+35) and ypurse-30 < yval < ypurse+30 and not pursedeleted:
			s.delete(purse) 
			itemscollected += 1
			pursedeleted = True

		if (xpainting-40 < xval < xpainting+35 or xpainting-40 <= xval+35 <= xpainting+35) and ypainting-30 < yval < ypainting+30 and not paintingdeleted:
			s.delete(painting) 
			itemscollected += 1
			paintingdeleted = True

		if (xdiamond-40 < xval < xdiamond+35 or xdiamond-40 <= xval+35 <= xdiamond+35) and ydiamond-30 < yval < ydiamond+30 and not diamonddeleted:
			s.delete(diamond) 
			itemscollected += 1
			diamonddeleted = True




# End of the game
def endGame():
	global homeb, nextb, buttontext

	# New mini screen
	s.create_rectangle(250,200, 550,350, fill = "lightsteelblue", outline = "slateblue", width = 5)
	s.create_line(250,250, 550,250, fill = "slateblue", width = 5)


	# If player pressed quit button, delete everything and take to home screen
	if pquit:
		s.delete("all")
		qbutton.destroy()
		intro()


	# If player didn't win, tell them they lost the level and restart+home buttons
	elif not won:
		qbutton.destroy()

		buttontext = ""
		s.create_text(400,230, text = "You Lost the Level.", font = "Times 17")
		
		homeb = Button(root, bg = "rosybrown2", activebackground = "rosybrown1", text = "Home", font = "Times 10", command = homescreen)
		homeb.place(x = 415,y = 265, width = 100, height = 60)
		
		nextb = Button(root, bg = "palegreen3", activebackground = "palegreen1", text = "Restart", font = "Times 10", command = nextLevel)
		nextb.place(x = 275,y = 265, width = 100, height = 60)


	# If player won and the level is 3, tell them they won the game and home button
	elif won and level == 3:
		qbutton.destroy()

		buttontext = ""
		s.create_text(400,230, text = "You Won the Game!", font = "Times 17")
		
		homeb = Button(root, bg = "rosybrown2", activebackground = "rosybrown1", text = "Home", font = "Times 10", command = homescreen)
		homeb.place(x = 300,y = 265, width = 200, height = 60)

	
	# If player won and the level is 1 or 2, tell them they won the level and next level + home button
	elif won and (level == 1 or level == 2):
		qbutton.destroy()

		buttontext = "Next Level"
		s.create_text(400,230, text = "You Won the Level!", font = "Times 17")
		
		homeb = Button(root, bg = "rosybrown2", activebackground = "rosybrown1", text = "Home", font = "Times 10", command = homescreen)
		homeb.place(x = 415,y = 265, width = 100, height = 60)
		
		nextb = Button(root, bg = "palegreen3", activebackground = "palegreen1", text = "Next Level", font = "Times 10", command = nextLevel)
		nextb.place(x = 275,y = 265, width = 100, height = 60)




# When next level button is clicked
def nextLevel():
	global level
	
	homeb.destroy()
	nextb.destroy()
	s.delete("all")
	
	# Change level if the button is a "next level" button
	if buttontext == "Next Level":
		if level == 1: level = 2
		elif level == 2: level = 3 

	runGame()




# When home button is clicked
def homescreen(): 
	s.delete("all")
	homeb.destroy()

	# Delete the next level/ restart button if it exists
	if level == 1 or level == 2 or not won: nextb.destroy()
	
	intro()




# Check to see if the player has won
def checkifwon():
	global won

	if level == 1:
		xadd = 55
		yadd = 145
	
	elif level == 2 or level == 3:
		xadd = 145
		yadd = 55

	# If all items collected and the player is between the door values defined above
	if ((doorx < xval < doorx+xadd or doorx < xval+25 < doorx+xadd) and (doory < yval < doory+yadd or doory < yval+25 < doory)) and lives > 0 and itemscollected == totalitems: won = True




# Check to see if the player has been caught by the guard
def checkifcaught():
	global caught, lives, itemscollected, cheesedeleted, shirtdeleted, shoedeleted, pursedeleted, paintingdeleted, diamonddeleted, xval, yval

	for i in range(numGuards):
		x = xguards[i]
		y = yguards[i]

		# Distance between player head and guard head
		d = sqrt((x-xval)**2 + (y-yval)**2)


		# Flashlight differences depending on direction
		if gdirections[i] == "up":
			ydiff1 = -100
			ydiff2 = 0
			xdiff1 = 0
			xdiff2 = 45
		
		elif gdirections[i] == "down":
			ydiff1 = 35
			ydiff2 = 120
			xdiff1 = 0
			xdiff2 = 45
		
		elif gdirections[i] == "left":
			ydiff1 = 0
			ydiff2 = 45
			xdiff1 = -74
			xdiff2 = 0
		
		elif gdirections[i] == "right":
			ydiff1 = 0
			ydiff2 = 45
			xdiff1 = 45
			xdiff2 = 129


		# If the player has touched the guard
		if d <= 35 or ((x+xdiff1 <= xval <= x+xdiff2 or x+xdiff1 <= xval+35 <= x+xdiff2) and y+ydiff1 <= yval <= y+ydiff2): 			
			
			# Reset position and decrease life
			xval = 25
			yval = 250
			lives -= 1


			# Return the items back to their spots depending on level
			if level == 1 and cheesedeleted:
				drawItems()
				itemscollected = 0
				cheesedeleted = False

			elif level == 2 and (shirtdeleted or shoedeleted):
				drawItems()
				itemscollected = 0
				shirtdeleted = False
				shoedeleted = False

			elif level == 3 and (pursedeleted or paintingdeleted or diamonddeleted):
				drawItems()
				itemscollected = 0
				pursedeleted = False
				paintingdeleted = False
				diamonddeleted = False 
			

			# "You lost a life" message
			rect = s.create_rectangle(400-100,270-50, 400+100,270+50, fill = "lightsteelblue", outline = "slateblue1", width = 5)
			text = s.create_text(400,270, text = "You lost a life!", font = "times 15")

			# Update, sleep, delete
			s.update()
			sleep(2)
			s.delete(rect,text)

			break




# Delete items of the level
def levelstuffdelete():
	if level == 1: s.delete(hcheese)
	elif level == 2: s.delete(hshoe,hshirt)
	elif level == 3: s.delete(hpurse, hpainting, hdiamond)








############# RUN GAME ##############

def runGame():

	# Initial functions
	setInitialvalues()
	drawBackground()
	drawItems()

	# Keeping game running while player has lives, hasn't won and hasn't quit yet
	while lives > 0 and not won and not pquit:
		drawHeader()
		drawPlayer()
		drawGuards()
		checkifcaught()
		checkifwon()

		# Update, sleep
		s.update()
		sleep(0.03)

		# Delete
		s.delete(head, mask1, mask2, eye1, eye2, header, livestext, ltext, livesr, itemstext)
		levelstuffdelete()
		for i in range(numGuards):
			s.delete(gheads[i], gcaps[i], gcaps2[i], geyesL[i], geyesR[i], gMsL[i], gMsR[i], gmouths[i], bodyf[i], bodyf2[i], light[i])


		# Updating
		updateplayer()
		updateguards()


	# After game ends
	drawHeader()
	endGame()








########### KEYBOARD EVENTS ############

# Arrow keys or "p" key pressed
def keyDownHandler(event):
	global xspeed, yspeed, pdirection

	# If moving player left
	if event.keysym == "Left" and xval > 0: 
		xspeed = -4
		pdirection = "left"

	# If moving player right
	elif event.keysym == "Right" and xval+45 < 800: 
		xspeed = 4
		pdirection = "right"

	# If moving player up
	elif event.keysym == "Up" and yval > 60: 
		yspeed = -4
		pdirection = "up"

	# If moving player down
	elif event.keysym == "Down" and yval+45 < 500: 
		yspeed = 4
		pdirection = "down"

	# If player wanting to pick something up
	elif event.keysym == "p": checkItem()
	



# Lifting the key after pressing- stop moving player
def keyUpHandler(event):
	global xspeed, yspeed, pdirection
	xspeed = 0
	yspeed = 0
	pdirection = "down"








############ SCREEN BINDING #############

root.after(0, intro)
s.bind("<Key>", keyDownHandler)
s.bind("<KeyRelease>", keyUpHandler)

s.pack()
s.focus_set()
root.mainloop()