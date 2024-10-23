from Account import Account
from Helper import HelperMethods

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # 1. Create an instance of the `Account` class and pass in the balance and interest parameters.
    acctCls = Account(balance,interest_rate)    
    #  Hint: You need to add the interest as a value, i.e, 0.
    interest_rate = float(interest_rate) 
    print(f"Interest_rate converted to float is: {interest_rate}")
    # 2. Create instance of Account cls    
    interest_Earned = HelperMethods.calcInterestEarned(balance,interest_rate,months)    
    # Update the savings account balance by adding the interest earned
    ## FIGURE OUT HOW TO ADD INT TO BALANCE
    balance = str(balance)
    balance += str(interest_Earned)
    print(f"balance w interest_earned is: {balance}")
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    acctCls.set_balance(float(balance))
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    acctCls.set_interest(interest_Earned)
    # Return the updated balance and interest earned.
    return balance