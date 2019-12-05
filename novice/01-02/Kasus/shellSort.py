def shellSort(A, n):
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap //= 2
A = [21,10,19,96,30,9,6,20,29]
size = len(A)
shellSort(A, size)
print(A)