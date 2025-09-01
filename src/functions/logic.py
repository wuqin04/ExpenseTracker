import customtkinter as ctk
import ui.widget as ui
from utils.helper import Direction, Debug

BALANCE_AMOUNT = 1000

def create_new_expense(main, create_new_expense):
    Debug("Creating New Expense")

    create_new_expense.configure(state="disabled")
    draw_expense_prompt = ui.ExpensePrompt(master=main)
    draw_expense_prompt.grid(row=5, column=0, sticky=Direction.UP)

def add_expense():
    Debug("Added Expenses")

def close_button(draw_expense_prompt):
    Debug("Closed Expense Prompt")

    draw_expense_prompt.destroy()