import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import Canvas
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import Checkbutton
from tkinter import Frame


from controller import ConnectFourController
from model import ConnectFourModel

class GameBoardView(tk.Frame):
    
    playerTurn = 'r'
    
    
    controller = 0;
    
    root = Tk();
    root.title("Connect Four");
    
    
    gameFrame = Frame(root);
    gameFrame.grid(row = 0, column = 0);
    
    
    gameCanvas = Canvas(gameFrame, bg = 'blue', width  =580, height = 500);
    
    
    gameCanvas.grid(row = 0, column = 0);
    
    scoreboardFrame = Frame(root);
    scoreboardFrame.grid(row =0, column = 1);
    
    turnIndicatorRow = 0;
    
    turnIndicatorLabel = Label(scoreboardFrame, text = "Red Player's\n Turn", fg = 'red', font = 'times 50', width = 10);
    turnIndicatorLabel.grid(row = turnIndicatorRow, column = 0, columnspan = 2, ipadx = 50);
    
    
    scoreLabelsRow = 1;
    
    redScoreLabel = Label(scoreboardFrame, text = "0", fg = 'red', font = 'times 80');
    redScoreLabel.grid(row = scoreLabelsRow, column = 0);
    
    yellowScoreLabel = Label(scoreboardFrame, text = "0", fg = 'black', font = 'times 80');
    yellowScoreLabel.grid(row = scoreLabelsRow, column = 1);
    
    
    
    
    returnToMenuButton = Button(scoreboardFrame, text = "Menu", font = 'times 40');
    returnToMenuButton.grid(row = 2, column = 0, columnspan = 2);
    
    circleSize = 30;
    
    
    def __init__(self, num_players):
        
        model = ConnectFourModel();
        model.set_observer(self);
        
        self.controller = ConnectFourController(model);
        
        
        
        self.gameCanvas.bind("<Button-1>", self.place_piece);
        
        
        
        
        
        for x in range(7):
            for y in range(6):
                xCoord  = x* 80 + 50;
                yCoord = y*80 + 50;
                
                self.gameCanvas.create_oval(xCoord - self.circleSize,yCoord -self.circleSize, xCoord +self.circleSize, yCoord +self.circleSize, outline = "#000", fill = 'white', width = 2);
        
        
        
        
        
        
        
        self.root.mainloop();
        
        pass

    def place_piece(self, event):
        """
        Callback function responsible for placing a piece.
        """
        # user move results in place_piece() call

        # set turn to black/red
        
        #if ai==true:
        #   controller.ai_move()
        
        
        #gets the column the user clicked
        columnClicked = (event.x - 20)//80;
        
        print(columnClicked);
        
        #make sure column selection is valid
        if(columnClicked < 0 or columnClicked > 6):
            return;
        
        #passes the move to the controller
        self.controller.place_piece(columnClicked, self.playerTurn);
        
        if(self.playerTurn == 'r'):
            self.playerTurn = 'b';
            self.turnIndicatorLabel.config( text = "Black Player's\n Turn", fg = 'black');
            
        elif(self.playerTurn == 'b'):
            self.playerTurn = 'r';
            self.turnIndicatorLabel.config( text = "Red Player's\n Turn", fg = 'red');
        
        
        
        
        pass

    def reset_score(self):
        """
        """
        pass

    def start_new_game(self):
        """
        """
        pass

    def quit_to_menu(self):
        """
        """
        pass

    def update(self):
        """
        
        """
        
        #get the grid from the model
        grid = self.controller.get_board();
        
        
        #for each circle
        for x in range(6):
            for y in range(7):
                
                #get the color
                color = grid[x][y];
                
                if(color == 'e'):
                    color = 'white';
                elif(color =='r'):
                    color = 'red';
                elif(color == 'b'):
                    color = 'black';
                
                
                
                #create circle of said color
                xCoord  = y* 80 + 50;
                yCoord = x*80 + 50;
                
                self.gameCanvas.create_oval(xCoord - self.circleSize,yCoord -self.circleSize, xCoord +self.circleSize, yCoord +self.circleSize, outline = "#000", fill = color, width = 2);
                
        pass
    
    
  
    
    
class MenuView(tk.Frame):

    def __init__(self):
        pass

    def start_game(self):
        """
        """
        pass

    def quit(self):
        """
        """
        pass
    
gameboard = GameBoardView(1);