from Accounts import Account
from Helper import HelperMethods

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # 1. Create an instance of the `Account` class and pass in the balance and interest parameters.
    acctCls = Account(balance,interest_rate) 
    # Hint: You need to add the interest as a value, i.e, 0.
    interest_rate = float(interest_rate)    
    # Calculate interest earned  
    interest_Earned = HelperMethods.calcInterestEarned(balance,interest_rate,months)
     # Update the cd account balance by adding the interest earned
    balance = str(balance)    
    balance = update_cd_account(balance,interest_Earned)   
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    acctCls.set_balance(float(balance))
    # Pass the updated_balance to the set balance method using the instance of the Account class.
    acctCls.set_balance(balance)
    # Pass the interest_earned to the set interest method using the instance of the Account class.
    acctCls.set_interest(interest_Earned)
    # Return the updated balance and interest earned.
    return balance, interest_Earned   

def update_cd_account(balance, interest_earned):
    # Initialize balance
    carried_balance = float(balance)
    if carried_balance > 0:
        deposit_balance = carried_balance + interest_earned
        print(f"The new balance of your cd account is ${float(deposit_balance):.2f}")
    else:
        print("Your deposit amount must be positive.")
    return deposit_balance

