import customtkinter as ctk

SIZE = "400x400"
TITLE = "ExpenseTracker"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(SIZE)
        self.title(TITLE)

app = App()
app.mainloop()