import customtkinter as ctk
from components.widget import Button
from functions.logic import add_expense

SIZE = "800x800"
TITLE = "ExpenseTracker"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(r"src/theme/default.json")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(SIZE)
        self.title(TITLE)
        
        self.add_expense = Button(self, text="Add Expense", command=add_expense)
        self.add_expense.place(relx=.5, y=700, anchor="center")

app = App()
app.mainloop()