import random

def main():
    print("*=*"*20)
    print("Welcome to the Dice simulator...")
    print("*=*"*20)
    print("\n")
    while True:
        inp = input("Press enter to roll the dice 1 and 2 (to quit, press q and enter):")
        if inp == 'q':
            print("Exiting dice simulator...")
            break
        n = random.randint(1,6)
        n1 = random.randint(1,6)
        print(n, ",", n1)    

if __name__ == '__main__':
    main()    





