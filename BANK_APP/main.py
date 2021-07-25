from bank import Bank

def main():
    print("BANK ACCOUNT SYSYTEM")
    print("-----------------------------------------")
    sbi_bank = Bank()

       
    sehar_customer = sbi_bank.add_customer("sehar")
    asvi_customer = sbi_bank.add_customer("asvi")
    alkesh_customer = sbi_bank.add_customer("alkesh")
    

    asvi_customer_savings_account = sbi_bank.add_account_to_customer(asvi_customer,"savings")

    alkesh_salary_account = sbi_bank.add_account_to_customer(alkesh_customer,"salary")

    sehar_customer_savings_account = sbi_bank.add_account_to_customer(sehar_customer,"savings")

    asvi_customer_trading_account = sbi_bank.add_account_to_customer(asvi_customer,"trading")

    alkesh_customer_savings_account = sbi_bank.add_account_to_customer(alkesh_customer,"savings")

    sehar_customer_trading_account = sbi_bank.add_account_to_customer(sehar_customer,"trading")

 
    sbi_bank.delete_account_from_customer(asvi_customer,asvi_customer_savings_account)

    sbi_bank.deposit_to_customer_account(sehar_customer , sehar_customer_trading_account,10000)

    sbi_bank.deposit_to_customer_account(sehar_customer , sehar_customer_savings_account,5000)

    sbi_bank.withdraw_from_customer_account(sehar_customer,sehar_customer_savings_account,100)

    sbi_bank.get_balance_in_customer_account(sehar_customer , sehar_customer_savings_account)
    

if __name__ == "__main__":

    main()    