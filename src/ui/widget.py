import customtkinter as ctk
import functions.logic as logic

class BalanceAmount(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            corner_radius=4,
            **kwargs
        )

        self.amount = ctk.CTkLabel(self, text=f"RM {logic.BALANCE_AMOUNT:,}", 
                                     width=250, height=80)
        self.amount.grid(row=0, column=0, padx=20)


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
            width=200,
            height=50,
            **kwargs
        )
