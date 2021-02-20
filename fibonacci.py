def fib(num):
    '''recursive functionn for generating 
    fibonacci sequence
    @pramas num: position till which series is printed
    @return recursivley calling previous values 
    and calculating fibonacci number at that position'''
    if(num==0)or(num==1):
        #base case
        return num; 
    #recursive call    
    fib1=fib(num-1)
    fib2=fib(num-2)
    return fib1+fib2


def test():
    '''function to test logic of fib() function'''
    assert fib(5)==5
    assert fib(7)==13
    print("all tests passed")

if __name__=="__main__":
    num=int(input("enter a number:"))
    for num in range(0,num):
        print(fib(num),end=" ")

    test()    

