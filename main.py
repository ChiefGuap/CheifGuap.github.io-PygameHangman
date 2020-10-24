import pygame
import os 
import math
import random

#ALL CAPS VARIABLES MEAN THEY ARE CONSTANT VALUES#

#SETUP DISPLAY#
#initializing the Pygame Module#
pygame.init()  
#Creating a width and height for the space that we can put stuff in#
WIDTH, HEIGHT = 800, 500
#Telling Pyagem to set up this display after running the code#
win = pygame.display.set_mode((WIDTH, HEIGHT))
#Defing the name of my game#
pygame.display.set_caption("Guapo Hangman")

#LOADING IMAGES FOR MY GAME#
#Creating a for loop for all 7 imaes, dont want to load each one of them one by one, takes to much work#
images = []
for i in range(7):
  image = pygame.image.load("hangman"+str(i)+".png")
  images.append(image)
#Images above will get loaded in as surface area images, have to add them within the pygame window of the game#

#BUTTON VARIABLES#
RADIUS = 20
GAP = 15
letters = [] #Example of what's being stored: [33, 46, "B", True]#
#Distance between the two buttons [at the very end and the very beggining of the row] is the equation that I ahve used below right here:(Width-(Gap-Raduis * 2)*13)/2#
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
  y = starty + ((i // 13) * (GAP + RADIUS * 2))
  letters.append([x, y, chr(A + i), True])

#Creating fonts for the game#
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('timesnewroman', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 60)
MESSAGE_FONT = pygame.font.SysFont('comicsans', 90)

#GAME VARIABLES#
man_status = 0
words = ["HELLO", "PYTHON", "RASHEDA", "DESIGN", "LEBRON", "ATTACK", "JUICE", "CODING", "RULER", "WHITEBOARD", "DEVELOPER", "FAIZATRASH"]
word = random.choice(words)
guessed = []

#COLORS#
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,100,0)

#CREATING A LOOP FOR OUR GAME, SO WE CAN RUN THIS GAME OVER AND OVER#
#Setting the speed for our game#
FPS = 60
#Make a clock object so that our loop runs at that speed#
clock = pygame.time.Clock()
run = True

#CREATING A FUNCTION DRAW EVERYTHING WITHIN THE PYGAME WINDOW#
def drawing():
  #Creating a background color for the game and updating display#
  win.fill((WHITE))

  #Drawing a main title for the game that will pop up within the window of the game#
  text = TITLE_FONT.render("Guapo Hangman", 1, BLACK)
  win.blit(text, (250, 20))


  #Drawing the lines for the word with a for loop#
  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word += "_ " 
  text = WORD_FONT.render(display_word, 1, BLACK)
  win.blit(text, (400, 200))     



  #drawing the buttons, with their respective cooridnates#
  for letter in letters:
    x, y, ltr, visible = letter
    if visible:
      #Drawing the circles within the window, with the color balck, and starting it from the center of the circle and thickness of circumference#
      pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
      text = LETTER_FONT.render(ltr, 1, BLACK)
      win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

  #Drawing the hangman image into the game using blit command#
  win.blit(images[man_status], (150,100))
  pygame.display.update()
  #Wanting to see every user event in the game. Every action done by the user#

#CREATING A FUNCTION TO DECLARE THE END MESSAGE OF THE GAME WETHER YOU WON OR LOST THE GAME#
def display_message(message):
  pygame.time.delay(3000)
  win.fill(WHITE)
  text = MESSAGE_FONT.render(message, 1, BLACK)
  win.blit(text, (280, 200))
  pygame.display.update()
  pygame.time.delay(3000)  
 

while run:
  #Making sure that our game runs at the speed given above#
  clock.tick(FPS)

  

  for event in pygame.event.get():
    #when we click on the quit buttton, the game should quit and while loop should also be finished#
    if event.type == pygame.QUIT:
      run = False
    #Following and tracking the mouse to see coordinates and actions of the mouse/cursor within the game#
    if event.type == pygame.MOUSEBUTTONDOWN:
      M_x, M_y = pygame.mouse.get_pos()
      for letter in letters:
        #Checking every single button and if the mouse button is within that radius and not outside that radius. Checking that collision#  
        x, y, ltr, visible = letter
        if visible:
          #To determine the distance between two points using the puthagoream theorem#
          DIS = math.sqrt((x-M_x) **2  + (y-M_y) **2 )
          if DIS < RADIUS:
            letter[3] = False
            print(ltr)
            guessed.append(ltr)
            if ltr not in word:
              man_status += 1
  drawing()            

  #Declaring if you won or lost the game# 
  won = True           
  for letter in word:
    if letter not in guessed:
      won = False
      break
  if won:  
    display_message("You Won!")
    break

  if man_status == 6:
    display_message("You Lost!")
    break   




#When we are done with the game or ready to quit#
#WHEN WE ARE DONE WITH THE GAME OR READY TO QUIT#
pygame.quit()

