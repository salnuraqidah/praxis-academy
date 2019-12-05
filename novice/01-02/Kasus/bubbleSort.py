def bubbleSort(A):
    n = len(A)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
 
# Driver code to test above
A = [21,10,19,96,30,9,6,20,29]
bubbleSort(A)
print(A)