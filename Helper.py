""" Create a helper class with methods"""
class HelperMethods:
    @staticmethod
    def calcInterestEarned(balance,interest_rate,months):
        bal = float(balance)
        intr = float(interest_rate)
        mths = float(months)       
        int_earned = bal * (intr/100 * mths/12)        
        #print(f"Interest_earned is: ${format(int_earned, ',.2f')}")
        return int_earned