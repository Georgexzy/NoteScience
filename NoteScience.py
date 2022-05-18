from cProfile import label
from cgitb import text
from struct import pack
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
from tkinter import font as tkFont
from tkinter import messagebox
root = tk.Tk()























filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile(): 
    global filename
    t = text.get(0.0,END)
    f = open (filename,"w")
    f.write(t)
    f.close()

def saveAs():
    f= asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
            showerror(title="Oops!", message="Unable to save file...")

def openFile():
 f = askopenfile(mode='r')
 t = f.read()
 text.delete(0.0, END)
 text.insert(0.0,t)

def add_highlighter():
      text.tag_add("start", "1.0","end")
      text.tag_configure("start",background="White", foreground= "Red")


def remove_highlighter():
      text.tag_add("start", "1.0","end")
      text.tag_configure("start", background="White", foreground= "Black")
    
   


def darkmode():
      if darkmode.get() == 1:
        root.config(background='black')

      elif darkmode.get() == 0:
        root.config(background='white')
      else:
        messagebox.showerror('PythonGuides', 'Something went wrong!')



darkmode = BooleanVar()
darkmode.set(False)

root.title("NoteScience Text Editor")
root.geometry("400x400")
text = Text ( root, height = 40)
text.pack()

Desired_font = tk.font.Font( family = "Times New Roman", 
                                 size = 13, 
                                 weight = "bold")
text.configure(font = Desired_font)





menubar = Menu(root)

viewmenu = Menu(menubar)
menubar.add_cascade(label="View",menu=viewmenu, underline=0)
viewmenu.add_checkbutton(label='darkmode', onvalue=1, offvalue=0, variable=darkmode, command=darkmode )


viewmenu.add_command(label="Highlight", command= add_highlighter)
viewmenu.add_command(label="Undo Highlight", command=remove_highlighter)



filemenu = Menu(menubar)

filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Save File", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)
root.config(menu=menubar)


root.mainloop()







