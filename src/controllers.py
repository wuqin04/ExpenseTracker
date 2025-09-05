import logic
from helper import Debug, Direction
from widget import ExpenseFrame, MessageBox

class ExpenseController:
    def __init__(self, master, balance_display, new_expense_button):

        # create all the widgets
        self.balance_display = balance_display
        self.new_expense_button = new_expense_button
        self.frame = ExpenseFrame(master=master, on_add=self.add, on_close=self.close)
        self.err_msg_box = MessageBox(master=master)

        # place all the widgets
        self.frame.show()
        
    def add(self, raw_input):
        is_valid, result = logic.validate_amount(raw_input)

        if not is_valid:
            self.err_msg_box.show(f"Error: {result}")
            self.close()
            return

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