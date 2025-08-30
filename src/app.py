import customtkinter as ctk
from components.widget import TotalAmount
from functions.logic import Direction


SIZE = "800x800"
TITLE = "ExpenseTracker"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(r"src/theme/default.json")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(SIZE)
        self.title(TITLE)
        self.grid_columnconfigure(0, weight=1)

        
        # init all the widgets
        self.total_amount = TotalAmount(self)

        # place all the widgets
        self.total_amount.grid(row=0, column=0, sticky=Direction.LEFT)

app = App()
app.mainloop()