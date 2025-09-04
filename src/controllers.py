import logic
from helper import Debug, Direction
from widget import ExpenseFrame

class ExpenseController:
    def __init__(self, master, balance_display, new_expense_button):

        # create all the widgets
        self.balance_display = balance_display
        self.new_expense_button = new_expense_button
        self.frame = ExpenseFrame(master=master, on_add=self.add, on_close=self.close)

        # place all the widgets
        self.frame.grid(row=5, column=0, sticky=Direction.UP)

    def add(self, raw_input):
        is_valid, result = logic.validate_amount(raw_input)

        if not is_valid:
            # show error message box in future
            pass

        Debug(f"RM{result:,.2f} is deducted.")

        # update balance amount 
        amount = result
        logic.update_balance(amount)
        self.balance_display.update_display(logic.BALANCE_AMOUNT)

        self.close()

    def close(self):
        Debug("Closed Expense Frame")

        self.frame.destroy()
        self.new_expense_button.configure(state="normal")