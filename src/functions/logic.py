import customtkinter as ctk
import ui.widget as ui
from utils.helper import Direction, Debug

BALANCE_AMOUNT = 1000

def create_new_expense(object, main):
    Debug("Creating New Expense")

    object.configure(state="disabled")

    draw_expense_prompt = ui.ExpensePrompt(master=main)
    draw_expense_prompt.grid(row=5, column=0, sticky=Direction.UP)

def add_expense():
    Debug("Added Expenses")

def close_button():
    Debug("Closed Expense Prompt")