from unittest import TestCase
class Account:
    def __init__(self,account_number,account_type):
        '''
        constructor for account class
        input : account number given to an account
        output : none
        '''
        self.account_number = account_number
        self.account_type = account_type
        

        self.balance = 0
        print("new account created of type:",account_type)


    def deposit(self,amount):
        '''
        function to add money in account
        input : amount to be added
        output : none
        '''    
        if isinstance(amount,int) or isinstance(amount,float):
            if amount < 0:
                print("please enter a positive amount")
            else:
                self.balance = self.balance + amount

        else:
            print("please enter a numeric value")        

    def withdraw(self,amount):
        '''
        function to withdraw money from account
        input : amount to be withdrawn
        output : none
        '''    
        if isinstance(amount,int) or isinstance(amount,float):


            if amount < 0:
                print("please enter a positive amount")
            else:
                self.balance = self.balance - amount

        else:
            print("please enter a numeric value") 
        

    def get_balance(self):
        '''
        function to get the balance in the account
        input: none
        output: current balance in account
        '''    
        return self.balance


class Account_test(TestCase):
    
    

    def test_deposit(self):
        account = Account(1,"savings")

        self.assertEqual(0,account.balance)
        account.deposit(500)
        self.assertEqual(500,account.balance)   

        account.deposit(-200)
        self.assertEqual(500,account.balance)

        account.deposit("lassi")
        self.assertEqual(500,account.balance)
        
        print("test passed")
    
    def test_withdraw(self):
        account = Account(1,"savings")
        account.deposit(500)

        self.assertEqual(500,account.balance)
        account.withdraw(200)

        self.assertEqual(300,account.balance)
        

        account.withdraw("lassi")
        self.assertEqual(300,account.balance)
        
        print("passed")



    def test_balance(self):
        account = Account(1,"savings")
        account.deposit(500)
        self.assertEqual(500,account.balance)
        account.withdraw(200)
        self.assertEqual(300,account.balance)

        account.get_balance()
        self.assertEqual(300,account.balance)
        print("passed")
        


        