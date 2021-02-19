def less_count(arr):
    arr_new=[]
    for i in arr:
        count=0
        
    
        for j in arr:
            if j<i:
                count+=1
        arr_new.append(count)
    for i in arr_new:
        print(i)

arr=[1,2,3,1]
less_count(arr)