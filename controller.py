class ConnectFourController():

    def __init__(self, model):
        self.model = model
        pass

    def get_board(self):
        return self.model.get_board()

    def clear_board(self):
        """
        """
        pass

    def place_piece(self, x, color):
        pass

    def has_won(self):
        """
        Returns 'r' if red has won, 'b' if black has won, NULL otherwise
        """
        pass

    def get_scores(self):
        """
        Returns [red score, black score]
        """
        return []

    def set_scores(self):
        pass

    def set_observer(self, observer):
        pass

    def ai_move(self):
        # does calculation

        # calls place_piece()
        pass
