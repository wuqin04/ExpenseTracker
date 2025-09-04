import customtkinter as ctk
import ui.widget as ui
from utils.helper import Direction, Debug

BALANCE_AMOUNT = 1000.00

def validate_amount(amount: float): 
    try:
        amount = float(amount)
    except ValueError:
        return (False, "Invalid amount.")
    
    if amount <= 0:
        return (False, "Amount must be greater than 0.")
    
    if amount > BALANCE_AMOUNT:
        return (False, "Insufficient balance.")
    
    return (True, f"RM{amount:,.2f}")
