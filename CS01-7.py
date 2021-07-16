
A = int(input("Please input first score : ")) 
B = int(input("Please input second score : "))
C = int(input("Please input third score : "))

if A or B or C <= 10:
    print("ไม่ผ่าน")    
if A or B or C <= 20:
    print("ปรับปรุง")    
if A or B or C <= 30:
    print("ดีมาก")    