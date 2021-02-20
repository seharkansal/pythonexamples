  
def primenumber(num):
    '''function to check if a give number is prime or not
    @pramas num:any number to be checked
    @return:num is prime or not
    '''
    if num >=2:  
        for i in range(2,num): 
            '''if num divides any number btw 2 nd itself 
            then it is not prime'''
            if (num % i) == 0:  
                return False 
    return True


def test():
    assert primenumber(11)==True
    assert primenumber(15)==False
    print("passed")    

if __name__=="__main__":
    number= int(input("number : "))  
    for i in range(2,number):
        if(primenumber(i)):
            print(i)
    test()        



 
