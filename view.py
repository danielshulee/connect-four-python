from textwrap import fill
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
from tkinter import messagebox
from tkinter.ttk import Style
from tkinter import PhotoImage

from PIL import Image,ImageTk

from controller import ConnectFourController
from model import ConnectFourModel




class GameBoardView(tk.Frame):
    
    num_players = 2 
    
    playerTurn = 'r'
    controller = 0 
    
    root = Tk() 
    root.title("Connect Four") 
  
    
  
    #gameboard
    gameBoardFrame = Frame(root) 
  
    
    
    gameFrame = Frame(gameBoardFrame) 
    gameFrame.grid(row = 0, column = 0) 
    
    gameCanvas = Canvas(gameFrame, bg = 'blue', width  =580, height = 500) 
    gameCanvas.grid(row = 0, column = 0) 
    
    scoreboardFrame = Frame(gameBoardFrame) 
    scoreboardFrame.grid(row =0, column = 1) 
    
    
    
    
    
    
    turnIndicatorRow = 0 
    
    turnIndicatorLabel = Label(scoreboardFrame, text = "Red Player's\n Turn", fg = 'red', font = 'times 50', width = 10) 
    turnIndicatorLabel.grid(row = turnIndicatorRow, column = 0, columnspan = 2, ipadx = 50) 
    
    
    scoreLabel = Label(scoreboardFrame, text = "Score:", font = 'times 30');
    scoreLabel.grid(row = 1, column = 0, columnspan = 2);
    
    
    
    scoreLabelsRow = 2 
    
    redScoreLabel = Label(scoreboardFrame, text = "0", fg = 'red', font = 'times 80') 
    redScoreLabel.grid(row = scoreLabelsRow, column = 0) 
    
    blackScoreLabel = Label(scoreboardFrame, text = "0", fg = 'black', font = 'times 80') 
    blackScoreLabel.grid(row = scoreLabelsRow, column = 1) 
    
    
    
    # Create menu
    menuFrame = Frame(root) 
    menuFrame.grid(row = 0, column = 0)
    
    menuCanvas = Canvas(menuFrame, width=580, height = 500)
    menuCanvas.pack()
    
    # Place background image in canvas
    background = ImageTk.PhotoImage(Image.open("connect-4-25.png").resize((580,500)))
    menuCanvas.create_image(0,0, anchor=NW, image=background)
    menuCanvas.create_text(290, 100, text="Welcome to Connect Four!", font=("Helvetica 33 bold"), fill="blue")
    menuCanvas.create_text(290,200, text="How many players?", font=("Helvetica 24 bold"))
    
    # menuLabel = Label(menuFrame, text = "Menu") 
    # menuLabel.grid(row = 0, column = 0) 
    
    onePlayerCheckbutton = None 
    twoPlayerCheckbutton = None 
    
    currentlyCheckedbutton = twoPlayerCheckbutton 
    
    circleSize = 30 
    
    
    def __init__(self):
        
       # model = ConnectFourModel() 
        #model.set_observer(self) 
        
        self.controller = ConnectFourController(ConnectFourModel()) 
        self.controller.set_observer(self) 
        
        self.gameCanvas.bind("<Button-1>", self.place_piece) 
        
        for x in range(7):
            for y in range(6):
                xCoord  = x* 80 + 50 
                yCoord = y*80 + 50 
                
                self.gameCanvas.create_oval(xCoord - self.circleSize,yCoord -self.circleSize, xCoord +self.circleSize, yCoord +self.circleSize, outline = "#000", fill = 'white', width = 2) 
        
        returnToMenuButton = Button(self.scoreboardFrame, text = "Menu", font = 'times 40', command = self.quit_to_menu) 
        returnToMenuButton.grid(row = 3, column = 0, columnspan = 2) 
        
        style = Style()
        style.configure("start-button", font = ("Helvetica 12 bold"))
        startNewGameButton = Button(self.menuFrame, text = "Start Game", height = 2, width=12, font=("Helvetica 20 bold"), command = self.start_game_from_menu) 
        # startNewGameButton.grid(row = 3, column = 0) 
        startNewGameButton.place(x=190,y=370)
        

        one_player_im = Image.open("1p.png").resize((30,60))
        one_player_imtk = ImageTk.PhotoImage(one_player_im)
        self.onePlayerCheckbutton = Checkbutton(self.menuFrame, image=one_player_imtk, command = self.onePlayerCheck) 
        self.onePlayerCheckbutton.place(x=160,y=260)
        
        two_player_im = Image.open("2p.png").resize((60,60))
        two_player_imtk = ImageTk.PhotoImage(two_player_im)
        self.twoPlayerCheckbutton = Checkbutton(self.menuFrame, image=two_player_imtk, command = self.twoPlayerCheck) 
        self.twoPlayerCheckbutton.place(x = 320, y = 260) 
        
        self.twoPlayerCheckbutton.select() 
        
        self.root.mainloop() 

    def place_piece(self, event):
        """
        Callback function responsible for placing a piece.
        """
        # user move results in place_piece() call

        # set turn to black/red
        
        #if ai==true:
        #   controller.ai_move()
        
        
        #gets the column the user clicked
        columnClicked = (event.x - 20)//80 
        
        
        
        #make sure column selection is valid
        if(columnClicked < 0 or columnClicked > 6):
            return 
        elif(self.controller.get_board()[0][columnClicked] != 'e'):
            return 
        
        
        
        #passes the move to the controller
        self.controller.place_piece(columnClicked, self.playerTurn)
            
        if(self.num_players == 2):
        
            if(self.playerTurn == 'r'):
                self.playerTurn = 'b' 
                self.turnIndicatorLabel.config( text = "Black Player's\n Turn", fg = 'black') 
                
            elif(self.playerTurn == 'b'):
                self.playerTurn = 'r' 
                self.turnIndicatorLabel.config( text = "Red Player's\n Turn", fg = 'red') 
        
        else:
            self.controller.ai_move()
        
        
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
        self.gameBoardFrame.grid_forget() 
        self.menuFrame.grid(row =0, column = 0) 
        
        pass

    def update(self):
        """
        
        """
        
        #get the grid from the model
        grid = self.controller.get_board() 
        
        
        #for each circle
        for x in range(6):
            for y in range(7):
                
                #get the color
                color = grid[x][y] 
                
                if(color == 'e'):
                    color = 'white' 
                elif(color =='r'):
                    color = 'red' 
                elif(color == 'b'):
                    color = 'black' 
                
                
                
                #create circle of said color
                xCoord  = y* 80 + 50 
                yCoord = x*80 + 50 
                
                self.gameCanvas.create_oval(xCoord - self.circleSize,yCoord -self.circleSize, xCoord +self.circleSize, yCoord +self.circleSize, outline = "#000", fill = color, width = 2) 
                
        
        
        scores = self.controller.get_scores() 
        
        self.redScoreLabel.config(text = scores[0]) 
        self.blackScoreLabel.config(text = scores[1]) 
        
        winner = self.controller.get_winner()
        if (winner == "r"):
            messagebox.showinfo("Winner!", "Red Player has won!")
            self.controller.clear_board() 
        elif (winner == "b"):
            if (self.num_players == 2):
                messagebox.showinfo("Winner!", "Black Player has won!")
            else:
                messagebox.showinfo("Loser!", "You Lost to the AI!")
            self.controller.clear_board()
        elif (winner == 't'):
            messagebox.showinfo("Tie!", "Neither Player has won!")
            self.controller.clear_board()

        pass

    
  
    def onePlayerCheck(self):
        
        
        if(self.currentlyCheckedbutton != self.onePlayerCheckbutton):
            
            self.num_players = 1 
            self.onePlayerCheckbutton.select() 
            self.twoPlayerCheckbutton.deselect() 
            self.currentlyCheckedbutton = self.onePlayerCheckbutton 
            
            
        
        
        pass
    

    def twoPlayerCheck(self):
        if(self.currentlyCheckedbutton != self.twoPlayerCheckbutton):
            
            self.num_players = 2 
            self.twoPlayerCheckbutton.select() 
            self.onePlayerCheckbutton.deselect() 
            self.currentlyCheckedbutton = self.twoPlayerCheckbutton 
        
        pass
    
   
   
    

    def start_game_from_menu(self):
        """
        """
        self.playerTurn = 'r' 
        self.turnIndicatorLabel.config( text = "Red Player's\n Turn", fg = 'red') 
        
        
        self.menuFrame.grid_forget() 
        self.gameBoardFrame.grid(row =0, column = 0) 
        self.controller.clear_board() 
        self.controller.set_scores(0, 0)
        self.update() 
        
        pass

    def quit(self):
        """
        """
        pass
    
gameboard = GameBoardView() 
