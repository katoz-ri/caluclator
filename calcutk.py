from tkinter import *
root=Tk()
def num(event):
    global val
    text=event.widget.cget("text")
    if text=="=":
        if val.get().isdigit():
            value=int(val.get())
        else:
            try:
                value=eval(screan.get())
                val.set(value)
            except:
                val.set("Syntax Error")
    elif text=="C":
        val.set("")
    elif text=="<-":
        val.set(val.get()[:-1])
    else:
        val.set(val.get()+text)
def fra():
    f=Frame(root)
    f.pack(side=LEFT,anchor="nw")
    return f
root.geometry("366x444")
root.maxsize(333,444)
root.minsize(366,444)
val=StringVar()
val.set("")
screan=Entry(root,text=val,bg="gray",fg="white",font="lucida 40 bold",borderwidth=6)
screan.pack(padx=10,pady=10)
l=[9,6,3,"=",8,5,2,0,7,4,1,"("," -"," *","+",")","C","<-"," / ","%"]
c=0
for i in l:
    if c%4==0:
        f=fra()
    c+=1
    b=Button(f,text=f"{i}",borderwidth=5,bg="yellow",font="lucida 20 bold")
    b.pack(padx=10,pady=10)
    b.bind("<Button-1>",num)
root.mainloop()