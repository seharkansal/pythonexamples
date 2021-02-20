
def matrix(size):
    '''function to print identity matrix of size n
    @prams size of identity matrix to be printed
    @return none
    '''
    for row in range(0,size):
        for col in range(0,size):
            if(row==col):
                '''if col=row size then 1 will be printed
                otherwise 0 will be printed everywhere else'''
                print("1",end=" ")
            else:
                print("0",end=" ")   
        print()    

def test():
    assert matrix(2)==[[1,0],
                       [0,1]]
    print("passed")


if __name__=="__main__":
    size=int(input("enter size:"))
    matrix(size)
    test()


