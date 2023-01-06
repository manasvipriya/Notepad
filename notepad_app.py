from tkinter.filedialog import *
import tkinter as tk
from tkinter import *
import os
from tkinter import messagebox


#defining functions:
#defining NEW
def newfile():
    global file
    canvas.title('untitled - Notepad')
    entry.delete(1.0,END)

#defining OPEN:
def openfile():
    global file
    file=askopenfilename(defaultextension='.txt', filetypes = [('text documents', '*.txt')])
    if file == " ":
        file= None

    else:
        canvas.title(os.path.basename(file) + ' -notepad')
        f = open(file, 'r')
        entry.insert(1.0, f.read())
        f.close()

#defining save
def savefile():
    global file
    file= asksaveasfilename(defaultextension='.txt', filetypes=[('All files','*.*'), ('text Document','*.txt')])
    if file == ' ':
            file = None
    else:
        f= open(file, 'w')
        f.write(entry.get(1.0, END))
        f.close()
#defining exit
def exitfile():
    canvas.destroy()


def cut():
    entry.event_generate(("<<Cut>>"))

def copy():
    entry.event_generate(("<<Copy>>"))

def paste():
    entry.event_generate(("<<Paste>>"))


def about_us():
    messagebox.showinfo('About us', 'This is a Python based notepad created with the help of tkinter library by Manasvi Priya')



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
file.add_command(label='New', command= newfile)
file.add_command(label='Save', command= savefile)
file.add_command(label='Open', command=openfile)
file.add_separator()
file.add_command(label='Exit', command=exitfile)
menubar.add_cascade(label='File',menu=file)


edit = Menu(menubar, tearoff=0)
edit.add_command(label='cut', command=cut)
edit.add_command(label='copy', command=copy)
edit.add_command(label='paste', command=paste)
menubar.add_cascade(label='Edit',menu=edit)

help = Menu(menubar, tearoff=0)
help.add_command(label="About Us", command=about_us)
menubar.add_cascade(label='Help', menu=help) 


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


