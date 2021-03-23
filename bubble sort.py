def bubble_sort(L):
    
    for itr in range(len(L)):
        #len(L)-itr-1 represents the number of times swapping will occur till the biggest elements goes in the end
        for j in range( len(L) - itr - 1):
            #check the adjacent elements
            if L[j] > L[j+1]:
                # pairwise swapping
                L[j] , L[j+1] = L[j+1] , L[j]


if __name__=="__main__":
    L = [19, 13, 6, 20, 18, 8]
    bubble_sort(L)
    print(L)  

