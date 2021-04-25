import random
def main():
    print("HELLO..")
    user=input("ENTER YOUR NAME:")
    print("OKAY",user," LETS PLAY HANGMAN!!!!")

    with open("words.txt","r") as file:
        allText=file.read()
        words=allText.split()
    test_word = random.choice(list(words))
    underscore = '_'
    lives=5

    guessed_word = list(underscore*len(test_word))

    print(*guessed_word,sep = " ")
    print()
    print("total lives:",lives)

    while True:
        print('==='*20)
        
        guess = input("guess a character:")
        if guess in test_word and guess != "" :
    
            for ind in range(len(test_word)):
                if test_word[ind] == guess:
                    guessed_word[ind] = guess
                    print()
            print(*guessed_word,sep =" ")
            print()
            print("WOW! GOOD GUESS..")

        else:
            print()
            print("OOPS! TRY AGAIN") 
            lives-=1
            print()
            print("lives left:",lives)
            if lives==2:
                index=guessed_word.index(underscore)
                hint=test_word[index]
                print("trying guessing:",hint)
      
            if lives==0:
                print()
                print("OOPS! YOU LOOSE..BETTER LUCK NEXT TIME...") 
                print("The original word was:",*test_word,sep="")   
                break       

        count1 = guessed_word.count(underscore)
        if count1 == 0:
            print()
            print("GOOD GAME",user,"!")  
            break 


if __name__=="__main__":
    main()             
                  
        
    





