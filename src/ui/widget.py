import customtkinter as ctk
import functions.logic as logic
from utils.helper import Direction

class BalanceAmount(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            **kwargs
        )
        
        # init
        self.amount = ctk.CTkLabel(self, text=f"RM {logic.BALANCE_AMOUNT:,}", 
                                     width=250, height=80)
        
        # place
        self.amount.grid(row=0, column=0, padx=20)

class ExpensePrompt(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color="#03045E",
            **kwargs
        )

        # init
        self.input_entry = ctk.CTkEntry(self, placeholder_text="Enter Amount",
                                        width=250, height=30)
        self.add_button = ctk.CTkButton(self, text="Add Expense",
                                        command=logic.add_expense)
        
        # place
        self.input_entry.grid(row=0, column=0, sticky=Direction.FILLED)
        self.grid_rowconfigure(0, weight=2)
        self.add_button.grid(row=1, column=0, sticky=Direction.UP)

class Button(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            width=200,
            height=80,
            **kwargs
        )

class InputEntry(ctk.CTkEntry):
    def __init__(self, master, on_clicked=None, **kwargs):
        super().__init__(
            master, 
            width=250,
            height=30,
            **kwargs
        )
