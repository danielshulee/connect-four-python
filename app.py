from view import GameBoardView


class App():
    def __init__(self):
        super().__init__()
        self.title('Connect 4')

        #---- create a view (tkinter frame) and place it in the root window
        view = GameBoardView(self)

app = App()
app.mainloop()