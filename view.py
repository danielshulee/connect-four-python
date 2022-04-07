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


class GameBoardView(tk.Frame):

    def __init__(self, num_players):
        root = Tk();
        root.title("Connect Four");
        
        gameFrame = Frame(root);
        gameFrame.grid(row = 0, column = 0);
        
        
        gameCanvas = Canvas(gameFrame, bg = 'blue', width  =580, height = 500);
        gameCanvas.grid(row = 0, column = 0);
        
        for x in range(7):
            for y in range(6):
                xCoord  = x* 80 + 50;
                yCoord = y*80 + 50;
                circleSize = 30;
                gameCanvas.create_oval(xCoord - circleSize,yCoord -circleSize, xCoord +circleSize, yCoord +circleSize, outline = "#000", fill = 'white', width = 2);
        
        
        
        scoreboardFrame = Frame(root);
        scoreboardFrame.grid(row =0, column = 1);
        
        turnIndicatorRow = 0;
        
        turnIndicatorLabel = Label(scoreboardFrame, text = "Red Player's\n Turn", fg = 'red', font = 'times 50');
        turnIndicatorLabel.grid(row = turnIndicatorRow, column = 0, columnspan = 2);
        
        
        scoreLabelsRow = 1;
        
        redScoreLabel = Label(scoreboardFrame, text = "0", fg = 'red', font = 'times 80');
        redScoreLabel.grid(row = scoreLabelsRow, column = 0);
        
        yellowScoreLabel = Label(scoreboardFrame, text = "0", fg = 'yellow', font = 'times 80');
        yellowScoreLabel.grid(row = scoreLabelsRow, column = 1);
        
        
        
        
        returnToMenuButton = Button(scoreboardFrame, text = "Menu", font = 'times 40');
        returnToMenuButton.grid(row = 2, column = 0, columnspan = 2);
        
        root.mainloop();
        
        pass

    def place_piece(self):
        """
        Callback function responsible for placing a piece.
        """
        # user move results in place_piece() call

        # set turn to black/red
        
        #if ai==true:
        #   controller.ai_move()

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