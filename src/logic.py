from helper import Debug

BALANCE_AMOUNT = 1000.00

def validate_amount(amount): 
    try:
        amount = float(amount)
    except ValueError:
        return (False, "Invalid amount.")
    
    if amount <= 0.00:
        return (False, "Amount must be greater than 0.")
    
    if amount > BALANCE_AMOUNT:
        return (False, "Insufficient balance.")
    
    return (True, amount)


def update_balance(amount):
    global BALANCE_AMOUNT
    BALANCE_AMOUNT -= amount
    Debug("balance amount updated")