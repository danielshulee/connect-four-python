import random

class ConnectFourController():
    """
    Controller for the connect four model. Contains methods to places pieces, clear
    board, check for winners, set player scores, and move according to ai.
    """

    def __init__(self, model):
        """
        Initializes an instance of this class with a model
        """
        self.model = model
        self.last_ai_move = None
        return

    def get_board(self):
        """
        Returns the board in 2d array form
        """
        return self.model.get_board()

    def clear_board(self):
        """
        Sets the board to an empty board
        """
        self.model.clear_board()

    def get_winner(self):
        """
        Returns which player won. r for red and b for black. Otherwise returns None.
        """
        return self.model.get_winner()

    def place_piece(self, col, color):
        """
        Places a piece given its color ('r' or 'b'), errors out otherwise )and column.
        Column zero is the leftmost column.
        Returns r if red won or b if black won or None if neither player has won from the move.
        """
        return self.model.place_piece(col, color, True)

    def get_scores(self):
        """
        Returns [red score, black score]
        """
        return self.model.get_scores()

    def set_scores(self, red_score, black_score):
        """
        Sets the scores for the red and black player
        """
        self.model.set_scores(red_score, black_score)

    def set_observer(self, observer):
        """
        Adds an observer to the list of observers for this model. Assumes an
        update() method.
        """
        self.model.set_observer(observer)

    def ai_move(self):
        """
        Calls on an AI (black) to place a piece on the board. The AI will look at the
        current board, choose a move, and place its piece by calling the `place_piece()`
        method.
        """
        # If first AI move, randomly place piece
        if self.last_ai_move == None: 
            col = random.randint(0,6)
            has_won = self.place_piece(col, 'b')
            self.last_ai_move = col
            return has_won
        # For every column, check if AI can win by placing piece
        moves = self.model.available_moves()
        for col in moves:
            if self.model.place_piece(col, 'b', False):
                return self.place_piece(col, 'b')
        # For every column, check if a move by the opponent would result in a victory
        # If so, play in that column
        for col in moves:
            if self.model.place_piece(col, 'r', False):
                has_won = self.place_piece(col, 'b')
                self.last_ai_move = col
                return has_won
        # Otherwise, randomly choose between the column last played in, the column to its
        # left, and column to its right
        next_moves = []
        # Case 1: last column is not filled
        if self.last_ai_move in moves:
            next_moves.append(self.last_ai_move)
        # Find closest column to left that isn't full (adds nothing if every column to left is full)
        lcol = self.last_ai_move-1
        while lcol >= 0:
            if lcol in moves:
                next_moves.append(lcol)
                break
            lcol -= 1
        # Repeat for right side
        rcol = self.last_ai_move+1
        while rcol < 7:
            if rcol in moves:
                next_moves.append(rcol)
                break
            rcol += 1
        # Choose from middle, left, and right columns
        index = random.randint(0, len(next_moves)-1)
        col = next_moves[index]
        has_won = self.place_piece(col,'b')
        self.last_ai_move = col
        return has_won

