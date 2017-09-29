from tkinter import *
import tkinter
tk=tkinter.Tk()
text1=Text(tk,height=20,width=30)
text1.pack()
with open('read.txt') as f:
    read_data=f.readlines()

for i in read_data:
    text1.insert(END,i)
def save():
    data=text1.get("1.0",END)
    with open('read.txt','w') as f:
        f.write(data)
button=Button(tk,text="SAVE",command=save)
button.pack()
tk.mainloop()
