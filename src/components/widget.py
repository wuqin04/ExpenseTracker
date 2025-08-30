import customtkinter as ctk
from functions.logic import Direction

class TotalAmount(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color="#04D4F0",
            corner_radius=4,
            **kwargs
        )

        self.amount = ctk.CTkLabel(self, text="RM 1,000", 
                                   text_color="#6AF2F0", width=250, height=80)
        self.amount.grid(row=0, column=0, padx=20)


class Button(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            width=200,
            height=80,
            **kwargs
        )

class Entry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(
            master, 
            width=200,
            height=50,
            **kwargs
        )