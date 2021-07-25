#three classes account, customer and bank, where a bank can have many
#customers and a customer can have many accounts 
#customer can add or delete his account
#bank can add or delete account of the customer
#account class for user to deposit money,
#withdraw money and check balance
from unittest import TestCase
from customer import Customer

class Bank:
    def __init__(self):
        '''
        constructoor of bank class
        input : none
        output : none
        '''        
        #empty dictionary  of customers
        
        self.customers = {}

        self.new_customer_id = 1
        

    def add_customer(self,name):
        '''
        function to add a new customer
        input : none
        output : customer numbr i.e. index of the the new customer created
        '''  

        #get customer number of the new customer to be added
        key = self.new_customer_id
        self.new_customer_id += 1

        #creating new instance (value)
        new_customer = Customer(name)

        #add this instance to the list of customers
        self.customers[key] = new_customer

        print("new customer created:",name)

        return key
        

    def delete_customer(self,key):
        '''
        function to delete a customer form the list of customers
        input : customer number of the customer to be deleted
        output : none
        '''
        #finding the customer to be deleted
        del self.customers[key]
        print("customer deleted",key)

    def add_account_to_customer(self, customer_number,account_type):
        '''
        function to add account to customer
        input : customer of which account needs to be added
        output : none
        '''
        print("------------------------------")
        print("new account created")
        customer = self.customers[customer_number]
        account_number = customer.add_account(account_type) 
        
        print("account number:",account_number,"for customer:",customer_number)
        return account_number 

    def delete_account_from_customer(self,customer_number,account_number):
        '''
        function to delete account from customer
        input: customer and its account number to be deleted
        output : none
        '''
        customer = self.customers[customer_number]
        customer.delete_account(account_number)   
        print("----------------------------------")
        print("deleted account from customer",customer_number,"'s account:",account_number)
        print("------------------------------------------")

    def deposit_to_customer_account(self,customer_number,account_number,amount):
        '''
        function to deposit money to a customer's account
        input : customer and its account to which money needs to be deposited
        output : none
        '''
        #get customer from customer list
        customer = self.customers[customer_number]
        
        #deposit money to that customer account
        customer.deposit_to_account(account_number,amount)
        
        #print("---------------------------------------------")
        print("money depsoited in account:",account_number,"by customer:",customer_number,"is",amount)
        print("---------------------------------------------")
        

    def withdraw_from_customer_account(self,customer_number,account_number,amount):
        '''
        function to withdraw money from a customer's account
        input : customer and account number from which money needs to be withdrawn
        output : none
        '''
        customer = self.customers[customer_number]
        customer.withdraw_from_account(account_number,amount)    
        print("money withdraw from account:",account_number,"by customer:",customer_number,"is",amount)
        print("-----------------------------------------------")

    def get_balance_in_customer_account(self,customer_number,account_number):
        '''
        function to get current balance of a customer's account
        input : customer and account number of which balance needs to be known
        output : current balance
        '''
        customer = self.customers[customer_number]
        customer_balance = customer.new_balance(account_number) 
        print("balance in account of customer",customer_number,"and  his account",account_number,"is",customer_balance)
        print("--------------------------------------------------")
        return customer_balance   


        
   
class Bank_test(TestCase):

    def test_add_customer(self):
        bank = Bank()
        self.assertEqual(0,len(bank.customers))

        bank.add_customer("sehar")
        self.assertEqual(1,len(bank.customers))

    def test_delete_customer(self):
        bank = Bank()
        bank = Bank()
        self.assertEqual(0,len(bank.customers))

        bank.add_customer("sehar")
        self.assertEqual(1,len(bank.customers))

        bank.delete_customer(1)
        self.assertEqual(0,len(bank.customers))
        

        

            





    









            