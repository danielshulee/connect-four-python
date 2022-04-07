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
        for i in range(6):
            board[i] = ["e"]*7
        return board;

    def place_piece(self, col, color):
        """
        Places a piece given its color ('r' or 'b'), errors out otherwise )and column.
        Column zero is the leftmost column.
        """
        if color != 'r' and color != 'b':
            assert False

        # TODO: implement "gravity"

        
        self.notify_observers()
        return

    def has_won(self):
        """
        Returns 'r' if red has won, 'b' if black has won, NULL otherwise.
        """
        # TODO
        # Search through entire array looking for four in a row of either color
        pass

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