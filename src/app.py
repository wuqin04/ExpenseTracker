import customtkinter as ctk
import logic as logic
from widget import DisplayBalance, ExpenseFrame, Button
from helper import Direction, Debug

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
        self.new_expense_button = Button(master=self, text="Create New Expense", 
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
        self.expense_frame = ExpenseFrame(master=self, on_save=self.save_expense,
                                          on_close=self.close_expense_frame)
        self.expense_frame.grid(row=5, column=0, sticky=Direction.UP)

    def save_expense(self):
        raw_amount = self.expense_frame.get_expense_amount()

        is_valid, result = logic.validate_amount(raw_amount)

        if not is_valid:
            # show error message box in future

            pass

        Debug(f"RM{result:,.2f} is deducted.")

        # update balance amount 
        amount = result
        logic.update_balance(amount)
        self.balance_display.update_display(logic.BALANCE_AMOUNT)
        
    def close_expense_frame(self):
        Debug("Closed Expense Frame")

        self.expense_frame.destroy()
        self.new_expense_button.configure(state="normal")

app = App()
app.mainloop()