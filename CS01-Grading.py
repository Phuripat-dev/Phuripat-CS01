A = int(input("คะแนนเก็บของนักเรียน : "))
B = int(input("คะแนนสอบกลางภาคของนักเรียน : "))
C = int(input("คะแนนสอบปลายภาคของนักเรียน : "))

if(A + B + C >= 80 and A + B + C < 100):
    print("เกรด A")
elif(A + B + C >= 75 and A + B + C <= 79):
    print("เกรด B+")
elif(A + B + C >= 70 and A + B + C <= 74):
    print("เกรด B")
elif(A + B + C >= 65 and A + B + C <= 69):
    print("เกรด C+")
elif(A + B + C >= 60 and A + B + C <= 64):
    print("เกรด C")
elif(A + B + C >= 55 and A + B + C <= 59):
    print("เกรด D+")
elif(A + B + C >= 50 and A + B + C <= 54):
    print("เกรด D")
elif(A + B + C >= 0 and A + B + C <= 49):
    print("เกรด F")