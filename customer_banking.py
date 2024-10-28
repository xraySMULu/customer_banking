# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.    
    savings_balance = input("Enter savings balance: ")
    savings_interest = input("Enter savings interest rate: ")
    savings_maturity = input("Enter savings maturity in months: ")
    # Call the create_savings_account function and pass the variables from the user.   
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # round value to 2 decimel            
    updated_savings_balance =str(updated_savings_balance) 
    updated_savings_balance = "{:,}".format(updated_savings_balance)
    # Print out the updated savings account balance with interest earned for the given months.
    print(f"Updated savings balance is: ${float(updated_savings_balance):.2f}")
    
    # round value to 2 decimel            
    interest_earned =str(interest_earned)  
    interest_earned = "{:,}".format(interest_earned)
    # Print out the interest earned for the given months.
    print(f"Interest earned is: ${float(interest_earned):.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input("Enter CD balance: ")
    cd_interest = input("Enter CD interest rate: ")
    cd_maturity = input("Enter CD maturity in months: ")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
 # round value to 2 decimel            
    updated_cd_balance =str(updated_cd_balance) 
    updated_cd_balance = "{:,}".format(updated_cd_balance)
    # Print out the updated CD balance with interest earned for the given months.
    print(f"Updated CD balance is: ${float(updated_cd_balance):.2f}")
    
    # round value to 2 decimel            
    interest_earned =str(interest_earned)  
    interest_earned = "{:,}".format(interest_earned)
    # Print out the interest earned for the given months.
    print(f"Interest earned is: ${float(interest_earned):.2f}")



if __name__ == "__main__":
   main()
