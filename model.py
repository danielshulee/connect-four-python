"""
Creates a ConnectFourModel class which represents the underlying connect four board
"""


class ConnectFourModel():
    """
    Model that represents connect four board. Contains methods to places pieces, clear
    board, check for winners, set player scores, and notify observers.
    """

    def __init__(self):
        """
        Initializes the model. The observers is set to empty, scores are set to 0 (red)
        vs 0 (black), and an empty board is created. For the representation of the
        board array and its conventions, see documentation for `create_empty_board()`.
        """
        self.observers = []
        self.scores = [0,0]
        self.height = 6
        self.width = 7
        self.clear_board()
        return

    def get_board(self):
        """
        Returns the board.
        """
        return self.board

    def clear_board(self):
        """
        Sets the board to an empty board
        """
        self.board = self.create_empty_board()

    def create_empty_board(self):
        """
        Creates an empty board. A board is 6 pieces (height) by 7 pieces (width),
        represented by an array with the following convention: the origin is set
        at the upper left hand tile, the first dimension moves vertically
        downward, and the second dimention moves horizontally to the right. For
        example, self.board[3,0] will return the piece in the fourth row and
        first column.

         _______________
        | 0,0  0,1  0,2
        | 1,0  1,1  1,2
        | 2,0  2,1  2,2

        Each element of the array contains a character string: "b" for black, "r"
        for red, and "e" for empty.
        """
        board = []
        for i in range(self.height):
            board.append(["e"]*self.width)
        return board

    def place_piece(self, col, color, notify):
        """
        Places a piece given its color ('r' or 'b'), errors out otherwise )and column.
        Notify should be true or false. If notify is true then the observer will be called
        to update the view.
        Column zero is the leftmost column.
        Returns r if red won or b if black won or NULL if neither player has won from the move.
        """
        if color != 'r' and color != 'b':
            assert False

        # Finds the lowest possible row a piece can be placed
        row = 0
        for i in range(self.height-1, -1, -1):
            if (self.board[i][col] == 'e'):
                self.board[i][col] = color
                row = i
                break
        
        # Winner has to be called before notify_observers, so that
        # score is updated before the observers are notified.
        winner = self.has_won(row, col)
        if notify:
            self.notify_observers()
        else:
            self.board[row][col] = 'e'

        return winner

    def has_won(self, row, col):
        """
        Checks if the piece placed at self.board[row][col] causes a player to win.
        If a player has won then the score is also updated.
        Returns 'r' if red has won, 'b' if black has won, None otherwise.
        """
        piece = self.board[row][col]
        pieces_amt = 1

        # Checks straights
        for i in range(1, 4):
            # Counts amount of pieces to the left of the placed piece
            if (col-i >= 0):
                if (self.board[row][col-i] == piece):
                    pieces_amt += 1
                else:
                    break
            else:
                break
        for i in range(1, 4):
            # Counts amount of pieces to the right of the placed piece
            if (col+i <= self.width-1):
                if (self.board[row][col+i] == piece):
                    pieces_amt += 1
                else:
                    break
            else:
                break
        if (pieces_amt >= 4):
            if piece == 'r':
                self.scores[0] += 1
            else:
                self.scores[1] += 1
            return piece
        pieces_amt = 1

        # Checks up and downs
        for i in range(1, 4):
            # Counts amount of pieces above the placed piece
            if (row-i >= 0):
                if (self.board[row-i][col] == piece):
                    pieces_amt += 1
                else:
                    break
            else:
                break
        for i in range(1, 4):
            # Counts amount of pieces below the placed piece
            if (row+i <= self.height-1):
                if (self.board[row+i][col] == piece):
                    pieces_amt += 1
                else:
                    break
            else:
                break
        if (pieces_amt >= 4):
            if piece == 'r':
                self.scores[0] += 1
            else:
                self.scores[1] += 1
            return piece
        pieces_amt = 1

        # Checks diagonals that goes from up-left to down-right
        for i in range(1, 4):
            # Counts amount of pieces to the diagonal-up-left
            if (row-i >= 0 and col-i >= 0):
                if (self.board[row-i][col-i] == piece):
                    pieces_amt += 1
                else:
                    break
            else:
                break
        for i in range(1, 4):
            # Counts amount of pieces to the diagonal-down-right
            if (row+i <= self.height-1 and col+i <= self.width-1):
                if (self.board[row+i][col+i] == piece):
                    pieces_amt += 1
                else:
                    break
            else:
                break
        if (pieces_amt >= 4):
            if piece == 'r':
                self.scores[0] += 1
            else:
                self.scores[1] += 1
            return piece
        pieces_amt = 1

        # Checks diagonals that goes from up-right to down-left
        for i in range(1, 4):
            # Counts amount of pieces to the diagonal-up-right
            if (row-i >= 0 and col+i <= self.width-1):
                if (self.board[row-i][col+i] == piece):
                    pieces_amt += 1
                else:
                    break
            else:
                break
        for i in range(1, 4):
            # Counts amount of pieces to the diagonal-down-left
            if (row+i <= self.height-1 and col-i >= 0):
                if (self.board[row+i][col-i] == piece):
                    pieces_amt += 1
                else:
                    break
            else:
                break
        if (pieces_amt >= 4):
            if piece == 'r':
                self.scores[0] += 1
            else:
                self.scores[1] += 1
            return piece
        pieces_amt = 1
                    
        return None

    def get_scores(self):
        """
        Returns [red score, black score]
        """
        return self.scores

    def set_scores(self, red_score, black_score):
        """
        Sets the scores for the red and black player
        """
        self.scores = [red_score, black_score]

    def set_observer(self, observer):
        """
        Adds an observer to the list of observers for this model. Assumes an
        update() method.
        """
        self.observers.append(observer)

    def notify_observers(self):
        """
        Notifies all observers of this model. Assumes that each observer has
        an update() method.
        """
        for ob in self.observers:
            ob.update()
        return

    def available_moves(self):
        """
        Return [0,1,2,4,5,6]
        """
        return