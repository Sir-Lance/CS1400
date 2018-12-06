#Lance Peters
#CS1400
#ProfessorAbrahamTeng
#Project 7 - Payrole Shuffle

import tkinter as tk
from tkinter import *
from tkinter import filedialog

class Erecord:
    def __init__(self, eId, eName, eAddress, eRate, eHour):
        self.id = eId
        self.name = eName
        self.address = eAddress
        self.rate = eRate
        self.hour = eHour

    def __str__(self):
        return "ID: " + str(self.id) + " Name: " + self.name

    def calc_salary(self):
        if self.hour <= 40:
            grossPay = self.rate * self.hour
        else:
            grossPay = self.rate*40 + 1.5*self.rate*(self.hour-40)

        stateTax = grossPay * 0.075
        fedTax = grossPay * 0.2
        netPay = grossPay - stateTax - fedTax
        return netPay

def main():
    root = Tk()
    menu = Menu(root)
    button = tk.Button(root, text="Next").pack()

    def OpenFile():
        root.filename = filedialog.askopenfilename(initialdir = "C:/",
            title = "Choose your file",
            filetypes = (("Text files","*.txt"),("all files","*.*")))
        if root.filename is (''):
            print("ERROR: No File Selected")
            root.quit
        else:
            print(root.filename, " ...File Loaded")
            file = open(root.filename, "w")

    def openGUI():
        root.config(menu = menu)
        filemenu  =  Menu(menu)
        menu.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "Open...", command = OpenFile)
        filemenu.add_command(label = "Exit", command = root.quit)

        root.mainloop()

    openGUI()

main()
