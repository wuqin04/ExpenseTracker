import customtkinter as ctk
import ui.widget as ui

BALANCE_AMOUNT = 1000

def add_expense(object):
    print("Adding Expense...")

    object.configure(state="disabled")

    get_user_expense = ui.InputEntry(master=object, placeholder_text="Enter Amount")
    