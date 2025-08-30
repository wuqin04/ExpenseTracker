import customtkinter as ctk
from utils.helper import *

BALANCE_AMOUNT = 1000

def add_expense(object):
    print("Adding Expense...")

    object.configure(state="disabled")