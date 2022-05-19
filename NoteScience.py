


#Importing Desired Modules

from cProfile import label
from cgitb import text
from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter.filedialog import *
from tkinter.font import Font
from tkinter import font as tkFont
from tkinter import colorchooser
from tkinter.messagebox import showerror
from turtle import clear
from typing import List    


root = tk.Tk()


root.configure(background='black')

our_font = font.Font(family="Helvetica", size="32")


my_listbox = Listbox(root, selectmode=SINGLE, width=275, height = 2)
my_listbox.pack()

for fnt in font.families():
    my_listbox.insert('end', fnt)


def font_chooser(event):
    our_font.config(
        family=my_listbox.get(my_listbox.curselection()))



my_listbox.bind('<ButtonRelease-1>', font_chooser)










filename = "Untitled"

#Defining Functions

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile(): 
    global filename
    t = text.get(0.0,END)
    f = open(filename + '.txt', 'w')
    f.write(t)
    f.close()

def saveAs():
    f= asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(tile="Oops!", message="Unable to save file...")


def openFile():
 f = askopenfile(mode='r')
 t = f.read()
 text.delete(0.0, END)
 text.insert(0.0,t)

def bolder():
    bold_font = font.Font(text, text.cget("font"))
    bold_font.configure(weight="bold")
  
    text.tag_config("bold", font = bold_font)
    current_tags = text.tag_names("sel.first")
    
    if "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    else:
          text.tag_add("bold", "sel.first", "sel.last")
    
def italicsiser():
    italics_font = font.Font(text, text.cget("font"))
    italics_font.configure(slant="italic")

    text.tag_configure("italics", font= italics_font)
    current_tags = text.tag_names("sel.first")
     
    if "italics" in current_tags:
        text.tag_remove("italics", "sel.first", "sel.last")
    else:
          text.tag_add("italics", "sel.first", "sel.last") 

def text_colour():
    my_colour = colorchooser.askcolor()[1]


    colour_font = font.Font(text, text.cget("font"))
    text.tag_configure("coloured", font=colour_font, foreground=my_colour)
    current_tags = text.tag_names("sel.first")
     
    if "coloured" in current_tags:
        text.tag_remove("coloured", "sel.first", "sel.last")
    else:
          text.tag_add("coloured", "sel.first", "sel.last") 

def background_colour():
     my_colour = colorchooser.askcolor()[1]
     if my_colour:
         text.config(bg=my_colour)

def all_text_colour():
    my_colour =colorchooser.askcolor()[1]
    if my_colour:
        text.config(fg=my_colour)

def select_all():
    text.tag_add('sel', '1.0', 'end')

def clear_all():
    text.delete(1.0, END)



scroll_bar = tk.Scrollbar(root)
scroll_bar.pack(side=tk.RIGHT)




#Creating the window

root.title("NoteScience Text Editor")
root.geometry("720x500")
text = Text ( root, height = 50, width = 100, undo=True, wrap="word", font=our_font)
text.pack()





#Menu Stuff
menubar = Menu(root)




viewmenu = Menu(menubar)
menubar.add_cascade(label="View",menu=viewmenu)
viewmenu.add_command(label="Bold", command=bolder)
viewmenu.add_command(label="Italics", command=italicsiser)
viewmenu.add_separator()
viewmenu.add_command(label= "Text Colour", command=text_colour)
viewmenu.add_command(label="Background Colour", command=background_colour)
viewmenu.add_command(label="All Text Colour", command=all_text_colour)
viewmenu.add_separator()
viewmenu.add_command(label="Select all", command=select_all)
viewmenu.add_command(label="Clear", command=clear_all )






menubar.add_command(label="Undo", command=text.edit_undo)
menubar.add_command(label="Redo", command=text.edit_redo)
 




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







