from tkinter import *

root=Tk()
root.geometry("250x300")
root.configure(bg="white")
root.title("Electronic Calculator")
root.resizable(False, False)

def show1(x):
    e1.insert(END, x)

e1=Entry(root, width=100, font=("Arial 18"))


def wipe1():
    e1.delete(0, END)

def result():
    answer=eval(e1.get())
    e1.delete(0, END)
    e1.insert(END, answer)

b9=Button(root, width=10, height=2, text="9", bg="white", command=lambda:show1(9))
b8=Button(root, width=10, height=2, text="8", bg="white", command=lambda:show1(8))
b7=Button(root, width=10, height=2, text="7", bg="white", command=lambda:show1(7))

b6=Button(root, width=10, height=2, text="6", bg="white", command=lambda:show1(6))
b5=Button(root, width=10, height=2, text="5", bg="white", command=lambda:show1(5))
b4=Button(root, width=10, height=2, text="4", bg="white", command=lambda:show1(4))

b3=Button(root, width=10, height=2, text="3", bg="white", command=lambda:show1(3))
b2=Button(root, width=10, height=2, text="2", bg="white", command=lambda:show1(2))
b1=Button(root, width=10, height=2, text="1", bg="white", command=lambda:show1(1))

b0=Button(root, width=10, height=2, text="0", bg="white", command=lambda:show1(0))
bplus=Button(root, width=10, height=2, text="+", bg="white",command=lambda:show1("+"))
bminus=Button(root, width=10, height=2, text="-", bg="white",command=lambda:show1("-"))

btimes=Button(root, width=10, height=2, text="X", bg="white",command=lambda:show1("*"))
bdivide=Button(root, width=10, height=2, text="/", bg="white",command=lambda:show1("/"))
bequals=Button(root, width=10, height=2, text="=", bg="white", command=result)

bclear=Button(root, width=31, height=2, text="clear", bg="white", command=wipe1)

b7.place(x=5, y=40)
b8.place(x=80, y=40)
b9.place(x=150, y=40)

b4.place(x=5, y=80)
b5.place(x=80, y=80)
b6.place(x=150, y=80)
#
b1.place(x=5, y=120)
b2.place(x=80, y=120)
b3.place(x=150, y=120)
#
b0.place(x=5, y=160)
bplus.place(x=80, y=160)
bminus.place(x=150, y=160)
#
btimes.place(x=5, y=200)
bdivide.place(x=80, y=200)
bequals.place(x=150, y=200)
#
bclear.place(x=5, y=240)

e1.place(x=2, y=2)
e1.config(state=DISABLED)

root.mainloop()
