import customtkinter as ctk
import functions.logic as logic
from ui.widget import DisplayBalance, ExpenseFrame, Button
from utils.helper import Direction, Debug

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
        self.balance_amount = DisplayBalance(master=self, balance=logic.BALANCE_AMOUNT)
        self.new_expense_button = Button(master=self, text="Create New Expense", 
                                  command=self.open_expense_frame)

        # place all the widgets
        self.grid_columnconfigure(0, weight=1)
        self.balance_amount.grid(row=0, column=0, sticky=Direction.LEFT)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.new_expense_button.grid(row=10, column=0, sticky=Direction.DOWN)

    def open_expense_frame(self):
        Debug("Open Expense Frame")

        self.new_expense_button.configure(state="disabled")
        self.expense_frame = ExpenseFrame(master=self, on_save=self.save_expense,
                                          on_close=self.close_expense_frame)
        self.expense_frame.grid(row=5, column=0, sticky=Direction.UP)

    def save_expense(self):
        
        self.expense_amount = self.expense_frame.get_expense_amount()
        Debug(f"You added RM{self.expense_amount}")

    def close_expense_frame(self):
        Debug("Closed Expense Frame")

        self.expense_frame.destroy()
        self.new_expense_button.configure(state="normal")

app = App()
app.mainloop()