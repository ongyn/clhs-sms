from os import system, name
import tkinter
from tkinter import messagebox
import string
def clear(): 
    if name == "nt": 
        _ = system("cls") 
    else: 
        _ = system("clear")
def msg(title, message):
    tmp = tkinter.Tk()
    tmp.withdraw()
    messagebox.showinfo(title, message)
def header():
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("\nDo you want to continue in GUI (Graphical User Interface) mode? Type Y for yes, N for no and C for credits.")
    answer = input("Input: ")
    if answer == "Y":
        system("gui.py")
    elif answer == "N":
        system("console.py")
    elif answer == "C":
        credit()
    else:
        msg("Warning", "Please enter a correct input.")
        header()
def credit():
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("\nDeveloper Team Members:")
    print("\033[1;34;40m\nONG YEAN\nLeader\nMain Programmer")
    print("\033[1;35;40m\nGOH SHENG FUNG\nProgrammer\nSlide Presenter")
    print("\033[1;33;40m\nCHEAH SHUANG QUAN\nFlow Chart & Pseudocode Designer\nSlide Presenter")
    print("\033[1;32;40m\nKHOO LI HENG\nFlow Chart & Pseudocode Main Designer")
    print("\033[1;31;40m\nKENG WEI XUAN\nSlide Creator\nSlide Presenter")
    print("\033[1;37;m\nInput anything to continue.")
    input("Input: ")
    header()
header()