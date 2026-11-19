#Four-in-a-row Challenge - www.101computing.net/four-in-a-row-challenge/
import turtle
from random import randint
from time import sleep
YELLOW=1
RED=2

#Draw the grid on screen with all the tokens
def drawGrid(grid):
  global RED, YELLOW
  #Clear the screen
  #myPen.clear()
  myPen.setheading(0)
  myPen.goto(-150,130)
  for row in range (0,6):
      for col in range (0,7):
            if grid[row][col]==0:
              myPen.fillcolor("#FFFFFF")
            elif grid[row][col]==RED:
              myPen.fillcolor("#FF0000")
            elif grid[row][col]==YELLOW:
              myPen.fillcolor("#FFFF00")
        
            myPen.begin_fill()
            myPen.circle(25)
            myPen.end_fill()
      
            myPen.penup()
            myPen.forward(50)
            myPen.pendown()	
      myPen.setheading(270) 
      myPen.penup()
      myPen.forward(50)
      myPen.setheading(180) 
      myPen.forward(50*7)
      myPen.setheading(0)
      myPen.getscreen().update()

def checkIfWinner(grid, color):
  #--------------------COMPLETE THE CODE HERE ---------------------------
  # Check if 4 in a row / column or diagonal
  # Returns color if so!
  #----------------------------------------------------------------------
  
  
  #Returns 0 if not
  for i in range(6):
    for j in range(3):
      if len(set([grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3]])) == 1:
        return grid[i][j]
  for i in range(2):
    for j in range(7):
      if len(set([grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]])) == 1:
        return grid[i][j]
  for i in range(2):
    for j in range(3):
      if len(set([grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]])) == 1:
        return grid[i][j]
  for i in range(3,6):
    for j in range(3):
      if len(set([grid[i][j], grid[i-1][j+1], grid[i-2][j+2], grid[i-3][j+3]])) == 1:
        return grid[i][j]
  return 0


#Main Program Starts Here
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(500)
window = turtle.Screen()
window.bgcolor("#2288FF")
myPen.color("#2288FF")
myPen.getscreen().tracer(0)
myPen.speed(0)

#Initialise empty 6 by 7 connect4 grid
connect4=[]
for row in range(0,6):
  connect4.append([])
  for col in range(0,7):
    connect4[row].append(0)

#Play the game, take it in turn. Up to 42 turns
for turn in range(1,43):
  #Randomly pick an column that is not full
  column = randint(0,6)
  while connect4[0][column]!=0:
    #This column is already full, pick another one
    column = randint(0,6)
  
  #Make the token slide to the bottom of the grid (Stacked on top of any other existing tokens)
  row=5
  while connect4[row][column]!=0:
    row=row - 1
  
  #Find out the colour of the current player (1 or 2)
  playerColor = (turn % 2) + 1
  #Place the token on the grid
  connect4[row][column]=playerColor
  #Draw the grid
  drawGrid(connect4)
  
  #Check if this token wins the game
  winner = checkIfWinner(connect4, playerColor)
  print(checkIfWinner(connect4, playerColor))  #e
  if winner==RED:
    myPen.penup()
    myPen.color("#FF0000")
    myPen.goto(-70, -170)
    myPen.write("RED Wins!", font="24pt")
    myPen.getscreen().update()
    break  #Stop the game
  elif winner==YELLOW:
    myPen.penup()
    myPen.color("#FFFF00")
    myPen.goto(-80, -170)
    myPen.write("Yellow Wins!", font="24pt") 
    myPen.getscreen().update()
    break  #Stop the game

  sleep(0.02)
sleep(2)
