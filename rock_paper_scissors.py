
import random

def main():
    while True:

        print("HELLO..")
        user = input("ENTER YOUR NAME:")
        print("OKAY",user," ROCK PAPER SCISSORS!!!!")
        print("enter P for paper, S for scissors and R for rock")
    
        while True:
            user = input("your turn:")
            choices = ["P","R","S"]
            if user in choices:
                break
            if user not in choices:
                print("please enter a valid letter")
        
    
        machine = random.choice(choices)
        

        if user == machine:
            print("machine's turn:",machine)
            print("OOPS! tie")

        elif(user == "P" and machine=="R"):
            print("machine's turn:",machine)
            print("WOHOO! you won")

        elif(user=="P" and machine=="S"):

            print("machine's turn:",machine)
            print("machine won")

        elif(user=="R" and machine=="P"):
            print("machine's turn:",machine)
            print("machine won")

        elif(user=="R" and machine=="S"):
            print("machine's turn:",machine)
            print("WOHOO! you won")

        elif(user=="S" and machine=="P"):
            print("machine's turn:",machine)
            print("WOHOO! you won")

        elif(user=="S" and machine=="R"):
            print("machine's turn:",machine)
            print("machine won")

        print("PLAY AGAIN?")
        print("[Y]/[N]") 
    
        final_choice=input("ENTER your choice:")   
        if final_choice!='Y':
            break


if __name__=='__main__':
    main()




