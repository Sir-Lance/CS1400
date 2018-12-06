import tkinter as tk
from tkinter import *
from tkinter import filedialog

def main():
    root = Tk()
    menu = Menu(root)

    def OpenFile():
        root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "Choose your file",filetypes = (("Text files","*.txt"),("all files","*.*")))
        if root.filename = ""

        print(root.filename, " ...File Loaded")

    def openGUI():
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open...", command=OpenFile)
        filemenu.add_command(label="Exit", command=root.quit)
        root.mainloop()

    openGUI()

main()
