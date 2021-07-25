from unittest import TestCase
from account import Account

class Customer:
    def __init__(self,name):
       '''
       constructor of customer class
       input : name of the customer
       output : none
       '''
       #self.name = name
        
       # empty dictionary of number of accounts
       self.accounts = {}
       self.name = name
       self.balance=0
       self.new_account_number = 1

    def add_account(self,account_type):
        '''
        function to add a new account by customer
        input : none
        output : account number i.e the index of new account created

        dictry ==> key, value
        key => the account number of the new aacount
        value ===> instance of account class
        '''
        #to get the account number of new account
        key = self.new_account_number
        self.new_account_number = self.new_account_number + 1

        #new instance i.e. the value in the dictionary
        new_account_instance = Account(key,account_type)
        
        #adding this new instance to total accounts
        self.accounts[key] = new_account_instance

        return key


    def delete_account(self,key):
        '''
        function to delete an account
        input : none
        output : none
        '''
        
        # find the account in the list of accounts to be deleted
        del self.accounts[key]

    def deposit_to_account(self,account_number,amount):
        '''
        function to add money in the account selected

        input: amount which needs to be added in selected account

        output : none
        '''
        target_account = self.accounts[account_number]

        target_account.deposit(amount)

    def withdraw_from_account(self,account_number,amount):
        '''
        function to withdraw money from the selected account
        input : amount which needs to be withdrawn from the account
        output : none
        '''

        target_account = self.accounts[account_number]

        target_account.withdraw(amount)   

    def new_balance(self,account_number):
        '''
        function to get the current available balance in the account
        input : account number of the account of which balance needs to be known
        output : current balance of the account
        '''
        target_account = self.accounts[account_number]
        balance = target_account.get_balance()
        return balance


class Customer_test(TestCase):

    def test_add_account(self):
        customer = Customer("sehar")
        self.assertEqual(0,len(customer.accounts) )

        customer.add_account("savings")   
        self.assertEqual(1,len(customer.accounts))
        
 

    def test_delete_account(self):
        customer = Customer("sehar")
        self.assertEqual(0,len(customer.accounts) )

        customer.add_account("savings")   
        self.assertEqual(1,len(customer.accounts))

        customer.delete_account(1)
        self.assertEqual(0,len(customer.accounts))


    def test_deposit_to_account(self):
        customer = Customer("sehar")
        self.assertEqual(0,len(customer.accounts) )

        customer.add_account("savings")   
        self.assertEqual(1,len(customer.accounts))

        customer.deposit_to_account(1,500)
        self.assertEqual(500,customer.balance)


  
  
        
