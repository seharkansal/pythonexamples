'''Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.

Input
Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

Output
Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

Example - Successful Transaction
Input:
30 120.00

Output:
89.50
Example - Incorrect Withdrawal Amount (not multiple of 5)
Input:
42 120.00

Output:
120.00
Example - Insufficient Funds
Input:
300 120.00

Output:
120.00'''
def withdraw(amount, balance):
    bankCharges=0.5
    #case1 amount>balance
    if (amount + bankCharges) > balance:
        return balance
    #case2 amount not multiple of 5
    if amount % 5 != 0:
        return balance
    #case3 amount ok
    else:
        totalMoney = balance - amount - bankCharges
        return totalMoney

def test_withdraw():
    result=withdraw(30,120)
    assert result==89.5
    result=withdraw(120,120)
    assert result==120
    result=withdraw(121,120)
    assert result==120
    print("test passed")

if __name__=="__main__":
    test_withdraw()
            

    

    



