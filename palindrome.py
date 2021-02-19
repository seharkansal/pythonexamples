  
from timeit import default_timer as timer

def palindrome(str):
    i=0
    j=len(str)-1
    while(i<j):
        if(str[i]==str[j]):
            i=i+1
            j=j-1

        else:
            return False
    return True            
    

s=input("enter a string:")
ans=palindrome(s)
if(ans):
    print("yes")
else:
    print("no")    

"""def test():
    
    result =  palindrome(10)
    assert len(result) == 10
    assert yay in result
    assert lost not in result
    print("All test passed.")"""

def test_performance():
    """
        Function to check the performance offollowing test cases
    """
    test_cases = ["bombay","madam","mom"]

    for test_case in test_cases:
        start = timer()
        result =  palindrome(test_case)
        end = timer() - start
        print("-"*20)
        print("Time Taken for gnerating ", test_case, " test case: ", end)
        print("-"*20)


if __name__=="__main__":
    #test()
    test_performance()  
