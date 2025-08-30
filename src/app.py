import customtkinter as ctk
from ui.widget import *
from functions.logic import *
from utils.helper import *

SIZE = "800x800"
TITLE = "ExpenseTracker"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(r"src/theme/default.json")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(SIZE)
        self.title(TITLE)
        
        # init all the widgets
        self.balance_amount = BalanceAmount(self)
        self.add_expense = Button(self, text="Add Expense", 
                                  command=lambda: add_expense(self.add_expense))

        # place all the widgets
        self.grid_columnconfigure(0, weight=1)
        self.balance_amount.grid(row=0, column=0, sticky=Direction.LEFT)

        self.grid_rowconfigure(9, weight=1)
        self.add_expense.grid(row=10, column=0, sticky=Direction.DOWN)


app = App()
app.mainloop()