from tkinter import*
root=Tk()
root.title("calculator")
root.geometry("600x700")
f=Frame(root,bg="black",bd=5,relief=GROOVE)
f.pack(fill="both",expand=True,padx=10,pady=10)
f1=Frame(f,bg="orange",bd=5,relief=GROOVE)
f1.pack(fill="both",expand=True,padx=10,pady=10)
def calc():
    root.geometry("500x600")
    frm=Frame(root,bg="grey",bd=5,relief=RIDGE)
    frm.pack(fill="both",expand=True,padx=10,pady=10)
    frm1=Frame(frm,bg="blue",bd=5,relief=RIDGE)
    frm1.pack(fill="both",expand=True,padx=10,pady=10)
    l1=Label(frm1,text="num1:",font=("arial",24))
    l2=Label(frm1,text="num2:",font=("arial",24))
    l1.grid()
    l2.grid()
    txt=Entry(frm1,width=20)
    txt.grid(row=0,column=1,padx=5,pady=5)
    txt1=Entry(frm1,width=20)
    txt1.grid(row=1,column=1,padx=5,pady=5)
    def display():
        try:
            n1=float(txt.get())
            n2=float(txt1.get())
            if n1==type(str) or n2==type(str):
                raise ValueError
            else:
                print("The sum is:",n2+n1)
        except ValueError:
            print("A word can't be calculated")
    def display1():
        try:
            n3=float(txt.get())
            n4=float(txt1.get())
            if n3==type(str) or n4==type(str):
                raise ValueError
            else:
                print("The difference is:",n3-n4)
        except ValueError:
            print("A word can't be calculated")
    def display2():
        try:
            n5=float(txt.get())
            n6=float(txt1.get())
            if n5==type(str) or n6==type(str):
                raise ValueError
            else:
                print("The product is:",n5*n6)
        except ValueError:
            print("A word can't be calculated")
    def display3():
        try:
            n7=float(txt.get())
            n8=float(txt1.get())
            if n8==0:
                raise TypeError
            elif n7==type(str) or n8==type(str):
                raise ValueError
            else:
                print("The remainder is:",n7/n8)
        except TypeError:
            print("The denominator cannot be zero")
        except ValueError:
            print("A word can't be calculated")
    x1=Button(frm1,text="addition",command=display,font=("arial",10))
    x1.grid(row=4,pady=10)
    x2=Button(frm1,text="subtraction",command=display1,font=("arial",10))
    x2.grid(row=5,pady=10)
    x3=Button(frm1,text="multiplication",command=display2,font=("arial",10))
    x3.grid(row=6,pady=10)
    x4=Button(frm1,text="division",command=display3,font=("arial",10))
    x4.grid(row=7,pady=10)
def methods():
    root.geometry("500x600")
    frm2=Frame(root,bg="grey",bd=5,relief=RIDGE)
    frm2.pack(fill="both",expand=True,padx=10,pady=10)
    frm3=Frame(frm2,bg="lightblue",bd=5,relief=RIDGE)
    frm3.pack(fill="both",expand=True,padx=10,pady=10)
    l=Label(frm3,text="num1:",font=("arial",24))
    l.grid() 
    txt2=Entry(frm3,width=20)
    txt2.grid(row=0,column=1,padx=5,pady=5)
    def display4():
        a=int(txt2.get())
        try:
            if a==0:
                raise TypeError
            elif a==type(str):
                raise ValueError
            else:
                print("The square is:",a*a)
        except TypeError:
            print("0 have no,square")
        except ValueError:
            print("A string can't have a square")
    def display5():
        try:
            a1=int(txt2.get())
            import math
            c=math.sqrt(a1)
            if a1==0:
                raise TypeError
            elif a1==type(str):
                raise ValueError
            else:
                print("The square root is:",c)
        except TypeError:
            print("0 have no,sqrt")
        except ValueError:
            print("A string can't have a sqrt")
    y=Button(frm3,text="square:",command=display4,font=("arial",10))
    y.grid(row=4,pady=10)
    y1=Button(frm3,text="squareroot",command=display5,font=("arial",10))
    y1.grid(row=5,pady=10)
b=Button(f1,text="Calculator",command=calc)
b.pack(side="top")
b1=Button(f1,text="other methods",command=methods)
b1.pack(side="top")
root.mainloop()


