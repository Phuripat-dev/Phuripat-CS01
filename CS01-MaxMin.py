Num = int(input("Enter your loop : "))
NumTotal = []
for i in range(Num):
  data = int(input("Enter your data : "))
  NumTotal += [data]
  NumTotal.sort()
m = NumTotal[0]
M = NumTotal[Num-1]
print(m)
print(M)