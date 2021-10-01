from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Calculator")
content = ""
txt = StringVar(value="0")

def btn(number):
    global content 
    content=content+str(number)
    txt.set(content)

def equal():
    global content 
    calculate=float(eval(content))
    txt.set(calculate)
    content = ""

def clear():
    global content 
    content = ""
    txt.set("")
    display.insert(0,"0")

display = Entry(font=("Helvetica",36,"normal"), width=14, fg="grey",bg="white", textvariable=txt,justify="right")
display.grid(row=0,columnspan=4)

Dot = ut0 = Button(width=1, height=1,fg="black",bg="lightgrey",font=("Helvetica",15,"normal"),text = ".", relief="flat", command = lambda:btn("."),padx=40,pady=15).grid(row=5,column=1)
Button0 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "0", relief="flat" , command = lambda:btn(0),padx=40,pady=15).grid(row=5,column=0)
Button1 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "1", relief="flat" , command = lambda:btn(1),padx=40,pady=15).grid(row=4,column=0)
Button2 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "2", relief="flat" , command = lambda:btn(2),padx=40,pady=15).grid(row=4,column=1)
Button3 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "3", relief="flat" , command = lambda:btn(3),padx=40,pady=15).grid(row=4,column=2)
Button4 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "4", relief="flat" , command = lambda:btn(4),padx=40,pady=15).grid(row=3,column=0)
Button5 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "5", relief="flat" , command = lambda:btn(5),padx=40,pady=15).grid(row=3,column=1)
Button6 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "6", relief="flat" , command = lambda:btn(6),padx=40,pady=15).grid(row=3,column=2)
Button7 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "7", relief="flat" , command = lambda:btn(7),padx=40,pady=15).grid(row=2,column=0)
Button8 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "8", relief="flat" , command = lambda:btn(8),padx=40,pady=15).grid(row=2,column=1)
Button9 = Button(width=1, height=1,fg="black", bg="lightgrey",font=("Helvetica",15,"normal"),text = "9", relief="flat" , command = lambda:btn(9),padx=40,pady=15).grid(row=2,column=2)

ClearButton= Button(width=1, height=1,fg="white", bg="grey",font=("Helvetica",15,"normal"),text = "C", command = clear,padx=40,pady=15).grid(row=1,column=0)
PlusButton= Button(width=1, height=1,fg="black", bg="orange",font=("Helvetica",15,"normal"),command = lambda:btn("+"),text = "+",padx=40,pady=15).grid(row=4,column=3)
MinusButton= Button(width=1, height=1,fg="black", bg="orange",font=("Helvetica",15,"normal"),command = lambda:btn("-"),text = "-",padx=40,pady=15).grid(row=3,column=3)
MultiplyButton= Button(width=1, height=1,fg="black", bg="orange",font=("Helvetica",15,"normal"),command = lambda:btn("*"),text = "×",padx=40,pady=15).grid(row=2,column=3)
DevideButton= Button(width=1, height=1,fg="black", bg="orange",font=("Helvetica",15,"normal"),command = lambda:btn("/"),text = "÷",padx=40,pady=15).grid(row=1,column=3)

EqualButton=Button(width=1, height=1,fg="black", bg="white",font=("Helvetica",15,"normal"),text="=",command=equal,padx=90,pady=15).grid(row=5,column=2,columnspan=2)
OpenParentheses=Button(width=1, height=1,fg="white", bg="grey",font=("Helvetica",15,"normal"),command = lambda:btn("("),text = "(",padx=40,pady=15).grid(row=1,column=1)
CloseParentheses= Button(width=1, height=1,fg="white", bg="grey",font=("Helvetica",15,"normal"),command = lambda:btn(")"),text = ")",padx=40,pady=15).grid(row=1,column=2)

root.mainloop()