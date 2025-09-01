import customtkinter as ctk
from ui.widget import BalanceAmount, Button
from functions.logic import create_new_expense
from utils.helper import Direction

SIZE = "800x800"
TITLE = "ExpenseTracker"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(r"src/theme/default.json")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(SIZE)
        self.title(TITLE)
        
        
        # draw all the widgets
        self.balance_amount = BalanceAmount(master=self)
        self.create_new_expense = Button(master=self, text="Create New Expense", 
                                  command=lambda: create_new_expense(self, self.create_new_expense))

        # place all the widgets
        self.grid_columnconfigure(0, weight=1)
        self.balance_amount.grid(row=0, column=0, sticky=Direction.LEFT)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.create_new_expense.grid(row=10, column=0, sticky=Direction.DOWN)


app = App()
app.mainloop()