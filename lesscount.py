from timeit import default_timer as timer

#function for less count 
def less_count(arr):
    arr_new=[]
    for i in arr:
        count=0 #intialize count variable to store less count
        
        for j in arr: #to iterate over the array
            if j<i:
                count+=1 #increment count for each less count
        arr_new.append(count) #store the count in new array
    for i in arr_new:
        print(i)

arr=[4,5,2,3]
less_count(arr)




def test_performance():
    """
        Function to check the performance offollowing test cases
    """
    test_cases = [[10000,20000,3000,40000],[10000,4,5,300]]

    for test_case in test_cases:
        start = timer()
        result =  less_count(test_case)
        end = timer() - start
        print("-"*20)
        print("Time Taken for gnerating ", test_case, " prime numbers: ", end)
        print("-"*20)


if __name__=="__main__":
    #test()
    test_performance()  
