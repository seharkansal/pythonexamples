  
from timeit import default_timer as timer

def palindrome(str):
    '''function iterates over a string if it is
    palindrome or not
    @pramas str:enter any string to check
    @return: true if palindrome and false if not
    '''
    i=0
    j=len(str)-1
    while(i<j):
        '''iterate over the string till middle element'''

        if(str[i]==str[j]):
            i=i+1
            j=j-1

        else:
            return False
    return True            
    

def test():
    str="bombay"
    assert palindrome(str)==False
    print("passed")

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
    s=input("enter a string:")
    ans=palindrome(s)
    if(ans):
        print("yes")
    else:
        print("no")  
    test()
    test_performance()  
