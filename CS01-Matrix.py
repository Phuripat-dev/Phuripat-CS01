import numpy as np
Array1 = []
Array2 = []
loop = 1
Rows = int(input("Input rows : "))
Columns = int(input("Input columns : "))
while( loop <= 2):
    print("Matrix [",loop,"] Input...")
    for r in range(Rows):
            print("[Row",r,"] Input ",Columns," numbers for each Column in a single line separated by space: ", end ="" )
            if (loop == 1):
                Array1Input = list(map(int, input().split()))
                Array1.append(Array1Input)
            else:
                Array2Input = list(map(int, input().split()))
                Array2.append(Array2Input)
    loop += 1
NumpyArray1 = np.asarray(Array1)
NumpyArray2 = np.asarray(Array2)
NewArray1 = NumpyArray1.reshape(Rows,Columns)
NewArray2 = NumpyArray2.reshape(Rows,Columns)
print("----------Matrix [1]----------")
print(NewArray1,"\n----------Matrix [2]----------")
print(NewArray2,"\n--------Sum of 2 Matrix-------")
sum = np.add(NewArray1, NewArray2)
print(sum,"\n------------------------------")