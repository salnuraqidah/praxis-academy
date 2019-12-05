# Selection sort
def selectionSort(A, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # To sort in descending order, change > to < in this line.
            if A[i] < A[min_idx]:
                min_idx = i
        (A[step], A[min_idx]) = (A[min_idx], A[step])
A = [21,10,19,96,30,9,6,20,29]
size = len(A)
selectionSort(A, size)
print(A)