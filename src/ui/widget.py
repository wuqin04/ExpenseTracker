import customtkinter as ctk
from utils.helper import Direction, Debug

# show the balance amount on the top-left of screen
class DisplayBalance(ctk.CTkFrame):
    def __init__(self, master, balance, **kwargs):
        super().__init__(
            master,
            **kwargs
        )
        
        # init
        self.balance = balance
        self.balance_label = ctk.CTkLabel(self, text=f"RM {self.balance:,}", 
                                     width=250, height=80)
        
        # place
        self.balance_label.grid(row=0, column=0, padx=20)

    def update_balance(self):
        pass

# draw the expense prompting 
class ExpenseFrame(ctk.CTkFrame):
    def __init__(self, master, on_save, on_close, **kwargs):
        super().__init__(
            master,
            fg_color="#03045E",
            **kwargs
        )

        # draw all the widgets
        self.expense_entry = ctk.CTkEntry(self, placeholder_text="Enter Amount",
                                        width=250, height=30)
        self.add_expense_button = ctk.CTkButton(self, text="Add Expense",
                                        command=on_save)
        self.close_button = ctk.CTkButton(self, text="X", width=40, height=15,
                                          command=on_close)
        
        # place all the widgets
        self.expense_entry.grid(row=1, column=1, sticky=Direction.FILLED)
        self.grid_rowconfigure(0, weight=2)
        self.add_expense_button.grid(row=2, column=1, sticky=Direction.UP)
        self.close_button.grid(row=0, column=2, sticky=Direction.RIGHT)

    def get_expense_amount(self):
        self.expense_amount = self.expense_entry.get()
        return self.expense_amount


class Button(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            width=200,
            height=80,
            **kwargs
        )