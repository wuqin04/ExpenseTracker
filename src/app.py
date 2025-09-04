import customtkinter as ctk
import logic as logic
from widget import DisplayBalance, ExpenseFrame, Button
from helper import Direction, Debug
from controllers import ExpenseController

SIZE = "600x600"
TITLE = "ExpenseTracker"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(r"src/theme/default.json")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(SIZE)
        self.title(TITLE)
        
        
        # draw all the widgets
        self.balance_display = DisplayBalance(master=self, balance=logic.BALANCE_AMOUNT)
        self.new_expense_button = Button(master=self, text="New Expense", 
                                  command=self.open_expense_frame)

        # place all the widgets
        self.grid_columnconfigure(0, weight=1)
        self.balance_display.grid(row=0, column=0, sticky=Direction.LEFT)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.new_expense_button.grid(row=10, column=0, sticky=Direction.DOWN)

    def open_expense_frame(self):
        Debug("Open Expense Frame")

        self.new_expense_button.configure(state="disabled")
        self.expense_controller = ExpenseController(self, self.balance_display, 
                                                    self.new_expense_button)

app = App()
app.mainloop()