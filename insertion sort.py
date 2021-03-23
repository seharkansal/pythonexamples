def insertion_sort(L):
    for i in range(1,len(L)):
        value = L[i]
        hole = i
        while hole > 0 and L[hole-1] > value:
            #shifting towards right till hole-1>value 
            L[hole] = L[hole-1]
            hole = hole-1
        #once hole-1 is not greater then value put the value in the current hole
        L[hole] = value


if __name__=="__main__":
    L = [3,2,4,5,11,45,23,12]
    print(L)
    insertion_sort(L)
    print(L)  

