import customtkinter as ctk
import ui.widget as ui
from utils.helper import Direction

BALANCE_AMOUNT = 1000

def create_new_expense(object, main):
    print("Adding Expense...")

    object.configure(state="disabled")

    get_user_expense = ui.ExpensePrompt(master=main)
    get_user_expense.grid(row=5, column=0, sticky=Direction.UP)

def add_expense():
    print("Added Expenses")