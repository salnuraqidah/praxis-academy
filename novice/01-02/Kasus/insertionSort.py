
def insertionSort(A):
   for i in range(1,len(A)):

     curNum = A[i]
     position = i

     while position>0 and A[position-1]>curNum:
         A[position]=A[position-1]
         position = position-1

     A[position]=curNum

A = [21,10,19,96,30,9,6,20,29]
insertionSort(A)
print(A)




