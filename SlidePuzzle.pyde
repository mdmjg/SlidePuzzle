add_library('sound')
import os
import random
path=os.getcwd()         #will give you the relative path of the file
numRows = 4
numCols = 4
position = 0



class Tile:
    def __init__(self, imageNum):
        self.imageNum = imageNum
        self.position = imageNum
        self.c = self.imageNum % 4 * 100
        self.r = self.imageNum / 4 * 100

    
    # display a tile if status is unhidden
    # @input:  self
    # @return: void
    def display (self):
        if self.imageNum < 15:
            img = loadImage(str(self.imageNum)+".png") #position of image
            image(img,self.c,self.r)
        else:
            fill(30,144,255)
            rect(self.c, self.r,100,100)
    
        
class Puzzle:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.board = []
        self.hiddenTileNum = 15 #We start with the hidden tile being in position 15
        self.createBoard()
        self.neighbors = []
        self.winSound = SoundFile(this,path+"\\TaDa.mp3")
        self.gameSound = SoundFile(this,path+"\\banana.mp3")
        if self.win == False:
            self.gameSound.play()
        
    def createBoard(self):
        for num in range(16): #We append all the images
           self.board.append(Tile(num))
        self.shuffle(2)
        self.win = False
        
                    
    def display(self):
        if self.win == False:
            for tile in self.board:
                tile.display()
        else: #load the last image
            for num in range(16):
                img = loadImage(str(num)+".png") #position of image
                image(img,num % 4 * 100, num / 4 * 100)
    
    def isValid(self, selectedTile): #Checks if the clicked tile is beside an empty tile
        hiddenTilePos = self.board[self.hiddenTileNum].position
        tempList = [-1,1,-4,4] #The hidden tile will be either to the right, to the left, at the top or at the bottom. If its one of the four then it returns true
        for num in tempList:
            if selectedTile.position + num == hiddenTilePos:
                return True
        return False
    
    def shuffle(self, difficulty):
        for a in range(difficulty):
            selectedTile = random.choice(self.getNeighbors())
            temp = selectedTile.imageNum
            a = selectedTile.position  
            selectedTile.imageNum = self.board[self.hiddenTileNum].imageNum
            self.board[self.hiddenTileNum].imageNum = temp
            self.hiddenTileNum = a
    
    def getNeighbors(self):
        coordinates = [-1, 1, -4, 4] #These are the four posible position surroundings of the tiles that could be swaped
        self.neighbors = []
        hiddenTilePos = self.board[self.hiddenTileNum].position
        for tile in self.board:
            for num in coordinates: #we loop through the coordinates
                if tile.position + num == hiddenTilePos: #If the tile happens to be beside, up or down from the hidden tile, we append th tile to the neighbors list
                    self.neighbors.append(tile)
        return self.neighbors
        
    
    def swap(self, selectedTile):
        if self.win == False:
            temp = selectedTile.imageNum
            a = selectedTile.position #Why are you not 
            selectedTile.imageNum = self.board[self.hiddenTileNum].imageNum
            self.board[self.hiddenTileNum].imageNum = temp
            self.hiddenTileNum = a
    
    def checkWin(self):
        for tile in self.board:
            if tile.position != tile.imageNum:
                self.win = False
                break
            else:
                self.win = True
    
                
                            
puzzle = Puzzle(numRows, numCols)

def setup():
    size(numCols*100, numRows*100)
    background(0)

def draw():
    puzzle.display()
    
def mouseClicked(): 
    for tile in puzzle.board: #We check which tile was clicked by comparing the x coordinated and the y coordinates
        if tile.c <= mouseX <= tile.c + 100 and tile.r <= mouseY <= tile.r+100:
            selectedTile = tile
    print(selectedTile.imageNum)
    if puzzle.isValid(selectedTile): #We check if the tile that was clicked is next to the empty tile, we have to convert these to a method called update.
        puzzle.swap(selectedTile)
    puzzle.checkWin()
    if puzzle.win == True:
        puzzle.gameSound.stop()
        puzzle.winSound.play()
        print("You won")

        
    