from tkinter.filedialog import *
import tkinter as tk
from tkinter import *


def saveFile():
    new_file = asksaveasfile(mode='w',filetypes=[("text files",".txt")])
    if new_file is None:
        return
    text = str(entry.get(1.0,END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode="r",filetypes=[("text files,".txt)])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)

def clearFile():
    entry.delete(1.0,END)



canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("My Notepad")
canvas.config(bg="white")
top=Frame(canvas)


scrollbar = Scrollbar(canvas)
scrollbar.pack(side=RIGHT, fill=Y)

menubar = Menu(canvas)
canvas.config(menu=menubar)

file = Menu(menubar, tearoff=0)
file.add_command(label='New')
file.add_command(label='Save')
file.add_command(label='Open')
file.add_separator()
file.add_command(label='Exit')
menubar.add_cascade(label='File',menu=file)


edit = Menu(menubar, tearoff=0)
edit.add_command(label='cut')
edit.add_command(label='copy')
edit.add_command(label='paste')
menubar.add_cascade(label='Edit',menu=edit)


help = Menu(menubar, tearoff=0)
help.add_command(label='Nothing')
menubar.add_cascade(label='Help',menu=help)

about = Menu(menubar, tearoff=0)
about.add_command(label='Author')
menubar.add_cascade(label='About me', menu=about)






'''b1= Button(canvas,text='Open',bg='white',command=openFile)
b1.pack(in_=top,side=LEFT)

b2=Button(canvas,text='Save',bg='white',command=saveFile)
b2.pack(in_=top,side=LEFT)

b3=Button(canvas,text='Clear',bg='white',command=clearFile)
b3.pack(in_=top,side=LEFT)

b4=Button(canvas,text='Exit',bg='white',command=exit)
b4.pack(in_=top,side=LEFT)'''

entry = Text(canvas, wrap=WORD, bg='#000000',font=("poppins",15),foreground ="white")
entry.pack(padx=0,pady=0,expand=TRUE,fill=BOTH)
canvas.mainloop()


