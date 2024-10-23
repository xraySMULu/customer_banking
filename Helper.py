""" Create a helper class with methods"""
class HelperMethods:
    @staticmethod
    def calcInterestEarned(balance,interest_rate,months):
        bal = float(balance)
        intr = float(interest_rate)
        mths = float(months)
        int_earned = (bal * mths * intr)/100
        int_earned = int_earned - bal 
        print(f"Simple interest_earned is: {int_earned}")
        return int_earned