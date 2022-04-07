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

    def place_piece(self, col, color):
        """
        Places a piece given its color ('r' or 'b'), errors out otherwise )and column.
        Column zero is the leftmost column.
        """
        self.model.place_piece(col, color)

    def has_won(self):
        """
        Returns 'r' if red has won, 'b' if black has won, NULL otherwise
        """
        return self.model.has_won()

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
        # TODO does calculation

        # calls place_piece()
        pass
