def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)-1):
      
        # let first element in the list be smallest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)-1):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        #swap sorted with unsorted element
        L[i], L[min_index] = L[min_index], L[i]


def test_selectionSort():
    L=[3,1,2,4]
    
    assert selection_sort(L)==[1,2,3,4]

    print("all test passed")


if __name__=="__main__":
    L=[3,1,2,4,5]
    selection_sort(L)
    print(L)
    test_selectionSort()
