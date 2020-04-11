# SCHOOL MANAGEMENT SYSTEM


# IMPORT LIBRARIES
from os import system, name
import tkinter
from tkinter import messagebox
from tkinter import *
import storage
import string
from threading import Timer


# GLOBAL VARIABLES
window = tkinter.Tk()
window2 = tkinter.Tk()
window2.withdraw()


# BASIC FUNCTIONS

# Sends a message to the user
def msg(title, message):
    tmp = tkinter.Tk()
    tmp.withdraw()
    messagebox.showinfo(title, message)

# Checks student ID validity
def checkID(sid):
    if sid.startswith("D") and len(sid) == 5:
        try:
            for x in range(4):
                _ = int(sid[x + 1])
        except:
            return False
        return True
    return False


# FUNCTIONS

# Loads login page
def loginPage():
    global window
    attempts = 3

    # Login Page: Event Listeners
    def onRegisterButtonClicked():
        window.withdraw()
        createAccountPage()
    def onLoginButtonClicked():
        nonlocal attempts
        sid = entry1.get()
        pwd = entry2.get()
        if storage.login(sid, pwd) == 0:
            if sid == "admin":
                adminPage()
            else:
                mainPage(sid)
        elif storage.login(sid, pwd) == 1:
            attempts = attempts - 1
            if attempts <= 0:
                msg("Warning", "The system is closing due to 3 wrong attempts.")
                exit()
            msg("Warning", "The student ID doesn't exist. " + str(attempts) + " attempts left.")
            window.focus_force()
        elif storage.login(sid, pwd) == 2:
            attempts = attempts - 1
            if attempts <= 0:
                msg("Warning", "The system is closing due to 3 wrong attempts.")
                exit()
            msg("Warning", "Your password is incorrect. " + str(attempts) + " attempts left.")
            window.focus_force()

    window.withdraw()
    window = tkinter.Tk()
    window.title("School Management System")
    window.geometry("640x480")
    window.resizable(False, False)
    label1 = Label(window, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window, text="Student ID:", font=("Arial Unicode MS", 16))
    label3.place(anchor=W, relx=0.11, rely=0.31)
    entry1 = Entry(window, font=("Arial Unicode MS", 14), width=32)
    entry1.place(anchor=E, relx=0.89, rely=0.31)
    label4 = Label(window, text="Password:", font=("Arial Unicode MS", 16))
    label4.place(anchor=W, relx=0.11, rely=0.41)
    entry2 = Entry(window, font=("Arial Unicode MS", 14), show="•", width=32)
    entry2.place(anchor=E, relx=0.89, rely=0.41)
    button1 = Button(window, text="I don't have an account", command=onRegisterButtonClicked, font=("Arial Unicode MS", 12), width=32, height=2)
    button1.place(anchor=W, relx=0.11, rely=0.61)
    button2 = Button(window, text="Login", command=onLoginButtonClicked, font=("Arial Unicode MS", 12), width=16, height=2)
    button2.place(anchor=E, relx=0.89, rely=0.61)
    window.bind("<Return>", (lambda e, b=button2: b.invoke()))
    entry1.focus_set()
    window.focus_force()
    window.mainloop()

# Loads create account page
def createAccountPage():
    global window

    # Create Account Page: Event Listener
    def onCreateButtonClicked():
        sid = entry1.get()
        pwd = entry2.get()
        cPwd = entry3.get()
        name = entry4.get()
        c = entry5.get()
        if not checkID(sid):
            msg("Warning", "Your Student ID is incorrect.")
            window.focus_force()
        elif pwd != cPwd:
            msg("Warning", "Password and confirmed password are not identical.")
            window.focus_force()
        elif pwd == "" and cPwd == "":
            msg("Warning", "Please input your password.")
            window.focus_force()
        elif name == "":
            msg("Warning", "Please input your name.")
            window.focus_force()
        elif c == "":
            msg("Warning", "Please input your class.")
            window.focus_force()
        elif storage.createID(sid, pwd, name, c) == 0:
            msg("Info", "Your account has been successfully created.")
            loginPage()
        else:
            msg("Warning", "Student already exists!")
            window.focus_force()

    window = tkinter.Tk()
    window.title("School Management System")
    window.geometry("640x480")
    window.resizable(False, False)
    label1 = Label(window, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window, text="Student ID:", font=("Arial Unicode MS", 16))
    label3.place(anchor=W, relx=0.06, rely=0.31)
    entry1 = Entry(window, font=("Arial Unicode MS", 14), width=32)
    entry1.place(anchor=E, relx=0.94, rely=0.31)
    label4 = Label(window, text="Password:", font=("Arial Unicode MS", 16))
    label4.place(anchor=W, relx=0.06, rely=0.41)
    entry2 = Entry(window, font=("Arial Unicode MS", 14), show="•", width=32)
    entry2.place(anchor=E, relx=0.94, rely=0.41)
    label5 = Label(window, text="Confirm Password:", font=("Arial Unicode MS", 16))
    label5.place(anchor=W, relx=0.06, rely=0.51)
    entry3 = Entry(window, font=("Arial Unicode MS", 14), show="•", width=32)
    entry3.place(anchor=E, relx=0.94, rely=0.51)
    label6 = Label(window, text="Name:", font=("Arial Unicode MS", 16))
    label6.place(anchor=W, relx=0.06, rely=0.61)
    entry4 = Entry(window, font=("Arial Unicode MS", 14), width=32)
    entry4.place(anchor=E, relx=0.94, rely=0.61)
    label7 = Label(window, text="Class:", font=("Arial Unicode MS", 16))
    label7.place(anchor=W, relx=0.06, rely=0.71)
    entry5 = Entry(window, font=("Arial Unicode MS", 14), width=32)
    entry5.place(anchor=E, relx=0.94, rely=0.71)
    button2 = Button(window, text="Create", command=onCreateButtonClicked, font=("Arial Unicode MS", 12), width=16, height=2)
    button2.place(anchor=E, relx=0.89, rely=0.86)
    window.bind("<Return>", (lambda e, b=button2: b.invoke()))
    entry1.focus_set()
    window.focus_force()
    window.mainloop()

# Loads main page
def mainPage(sid):
    global window

    # Main Page: Event Listener
    def onLogOutButtonClicked():
        storage.logout()
        msg("Info", "Successfully logged out.")
        loginPage()
    def onExamButtonClicked():
        window.withdraw()
        examPage(sid)
    def onCoButtonClicked():
        window.withdraw()
        coPage(sid)
    def onChangePasswordButtonClicked():
        window.withdraw()
        changePasswordPage(sid)

    window.withdraw()
    window = tkinter.Tk()
    window.title("School Management System")
    window.geometry("640x480")
    window.resizable(False, False)
    label1 = Label(window, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window, text="Student Name: " + storage.getName() + "            Class: " + storage.getClass(), font=("Arial Unicode MS", 12))
    label3.place(anchor=W, relx=0.01, rely=0.21)
    button1 = Button(window, text="Log Out", command=onLogOutButtonClicked, font=("Arial Unicode MS", 8))
    button1.place(anchor=E, relx=0.99, rely=0.21)
    frame1 = Frame(window)
    frame1.place(anchor=N, relx=0.5, rely=0.31)
    button2 = Button(frame1, text="Check exam result", command=onExamButtonClicked, font=("Arial Unicode MS", 16))
    button2.grid(row=0, column=0, pady=3)
    button3 = Button(frame1, text="Check cocurriculum info", command=onCoButtonClicked, font=("Arial Unicode MS", 16))
    button3.grid(row=1, column=0, pady=3)
    button4 = Button(frame1, text="Change password", command=onChangePasswordButtonClicked, font=("Arial Unicode MS", 16))
    button4.grid(row=2, column=0, pady=3)
    window.bind("<Return>", (lambda e: None))
    window.focus_force()
    window.mainloop()

# Shows exam result page
def examPage(sid):
    global window2

    # Exam Result Page: Event Listener
    def onBackButtonClicked():
        window2.withdraw()
        mainPage(sid)

    window2 = tkinter.Tk()
    window2.title("School Management System")
    window2.geometry("640x480")
    window2.resizable(False, False)
    label1 = Label(window2, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window2, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window2, text="Student Name: " + storage.getName() + "            Class: " + storage.getClass(), font=("Arial Unicode MS", 12))
    label3.place(anchor=W, relx=0.01, rely=0.21)
    button1 = Button(window2, text="Back", command=onBackButtonClicked, font=("Arial Unicode MS", 8))
    button1.place(anchor=E, relx=0.99, rely=0.21)
    frame1 = Frame(window2)
    frame1.place(anchor=N, relx=0.5, rely=0.26)
    label4 = Label(frame1, text="First Test", font=("Arial", 12))
    label4.grid(row=0, column=1, padx=32)
    label5 = Label(frame1, text="First Exam", font=("Arial", 12))
    label5.grid(row=0, column=2, padx=32)
    label6 = Label(frame1, text="Second Test", font=("Arial", 12))
    label6.grid(row=0, column=3, padx=32)
    label7 = Label(frame1, text="Final Exam", font=("Arial", 12))
    label7.grid(row=0, column=4, padx=32)
    label8 = Label(frame1, text="BC", font=("Arial", 12))
    label8.grid(row=1, column=0, pady=1)
    label9 = Label(frame1, text="BM", font=("Arial", 12))
    label9.grid(row=2, column=0, pady=1)
    label10 = Label(frame1, text="BI", font=("Arial", 12))
    label10.grid(row=3, column=0, pady=1)
    label11 = Label(frame1, text="MM", font=("Arial", 12))
    label11.grid(row=4, column=0, pady=1)
    label12 = Label(frame1, text="SC", font=("Arial", 12))
    label12.grid(row=5, column=0, pady=1)
    label13 = Label(frame1, text="ASK", font=("Arial", 12))
    label13.grid(row=6, column=0, pady=1)
    label14 = Label(frame1, text="SJ", font=("Arial", 12))
    label14.grid(row=7, column=0, pady=1)
    label15 = Label(frame1, text="GE", font=("Arial", 12))
    label15.grid(row=8, column=0, pady=1)
    label16 = Label(frame1, text="PM", font=("Arial", 12))
    label16.grid(row=9, column=0, pady=1)
    label17 = Label(frame1, text="PJK", font=("Arial", 12))
    label17.grid(row=10, column=0, pady=1)
    label18 = Label(frame1, text="PSV", font=("Arial", 12))
    label18.grid(row=11, column=0, pady=1)
    result = storage.getExamResult()
    for x in range(9):
        labelResult = Label(frame1, text=result[x], font=("Arial", 12))
        labelResult.grid(row=x + 1, column=1, padx=32, pady=3)
    for x in range(11):
        labelResult = Label(frame1, text=result[x + 9], font=("Arial", 12))
        labelResult.grid(row=x + 1, column=2, padx=32, pady=3)
    for x in range(9):
        labelResult = Label(frame1, text=result[x + 20], font=("Arial", 12))
        labelResult.grid(row=x + 1, column=3, padx=32, pady=3)
    for x in range(11):
        labelResult = Label(frame1, text=result[x + 29], font=("Arial", 12))
        labelResult.grid(row=x + 1, column=4, padx=32, pady=3)
    window.bind("<Return>", (lambda e: None))
    window2.focus_force()
    window2.mainloop()

# Shows cocurriculum page
def coPage(sid):
    global window2

    # Cocurriculum Page: Event Listener
    def onBackButtonClicked():
        window2.withdraw()
        mainPage(sid)

    window2 = tkinter.Tk()
    window2.title("School Management System")
    window2.geometry("960x480")
    window2.resizable(False, False)
    label1 = Label(window2, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window2, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window2, text="Student Name: " + storage.getName() + "            Class: " + storage.getClass(), font=("Arial Unicode MS", 12))
    label3.place(anchor=W, relx=0.01, rely=0.21)
    button1 = Button(window2, text="Back", command=onBackButtonClicked, font=("Arial Unicode MS", 8))
    button1.place(anchor=E, relx=0.99, rely=0.21)
    frame1 = Frame(window2)
    frame1.place(anchor=N, relx=0.5, rely=0.26)
    label4 = Label(frame1, text="Name", font=("Arial", 12))
    label4.grid(row=0, column=0, padx=64)
    label5 = Label(frame1, text="Category", font=("Arial", 12))
    label5.grid(row=0, column=1, padx=64)
    label6 = Label(frame1, text="Pose", font=("Arial", 12))
    label6.grid(row=0, column=2, padx=32)
    label7 = Label(frame1, text="Marks", font=("Arial", 12))
    label7.grid(row=0, column=3, padx=4)
    co = storage.getCocurriculum()
    label8 = Label(frame1, text=co[0], font=("Arial", 12))
    label8.grid(row=1, column=0, pady=4)
    label9 = Label(frame1, text="Pakaian Beruniform", font=("Arial", 12))
    label9.grid(row=1, column=1, pady=1)
    label10 = Label(frame1, text=co[1], font=("Arial", 12))
    label10.grid(row=1, column=2, pady=1)
    label11 = Label(frame1, text=co[2], font=("Arial", 12))
    label11.grid(row=1, column=3, pady=1)
    label12 = Label(frame1, text=co[3], font=("Arial", 12))
    label12.grid(row=2, column=0, pady=1)
    label13 = Label(frame1, text="Persatuan", font=("Arial", 12))
    label13.grid(row=2, column=1, pady=1)
    label14 = Label(frame1, text=co[4], font=("Arial", 12))
    label14.grid(row=2, column=2, pady=1)
    label15 = Label(frame1, text=co[5], font=("Arial", 12))
    label15.grid(row=2, column=3, pady=1)
    label16 = Label(frame1, text=co[6], font=("Arial", 12))
    label16.grid(row=3, column=0, pady=1)
    label17 = Label(frame1, text="Sukan/Permainan", font=("Arial", 12))
    label17.grid(row=3, column=1, pady=1)
    label18 = Label(frame1, text=co[7], font=("Arial", 12))
    label18.grid(row=3, column=2, pady=1)
    label19 = Label(frame1, text=co[8], font=("Arial", 12))
    label19.grid(row=3, column=3, pady=1)
    window.bind("<Return>", (lambda e: None))
    window2.focus_force()
    window2.mainloop()

def changePasswordPage(sid):
    global window2

    # Change Password Page: Event Listener
    def onBackButtonClicked():
        window2.withdraw()
        mainPage(sid)
    def onChangeButtonClicked():
        oldPwd = entry1.get()
        newPwd = entry2.get()
        cPwd = entry3.get()
        if newPwd != cPwd:
            msg("Warning", "Password and confirmed password are not identical.")
            window2.focus_force()
        elif newPwd == "" and cPwd == "":
            msg("Warning", "Please input your new password.")
            window2.focus_force()
        elif storage.changePassword(sid, oldPwd, newPwd) == 0:
            msg("Info", "Your password has been successfully changed.")
            onBackButtonClicked()
        else:
            msg("Warning", "Your old password is incorrect.")
            window2.focus_force()
        

    window2 = tkinter.Tk()
    window2.title("School Management System")
    window2.geometry("640x480")
    window2.resizable(False, False)
    label1 = Label(window2, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window2, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window2, text="Student Name: " + storage.getName() + "            Class: " + storage.getClass(), font=("Arial Unicode MS", 12))
    label3.place(anchor=W, relx=0.01, rely=0.21)
    button1 = Button(window2, text="Back", command=onBackButtonClicked, font=("Arial Unicode MS", 8))
    button1.place(anchor=E, relx=0.99, rely=0.21)
    label4 = Label(window2, text="Old Password:", font=("Arial Unicode MS", 16))
    label4.place(anchor=W, relx=0.06, rely=0.31)
    entry1 = Entry(window2, font=("Arial Unicode MS", 14), show="•", width=32)
    entry1.place(anchor=E, relx=0.94, rely=0.31)
    label5 = Label(window2, text="New Password:", font=("Arial Unicode MS", 16))
    label5.place(anchor=W, relx=0.06, rely=0.41)
    entry2 = Entry(window2, font=("Arial Unicode MS", 14), show="•", width=32)
    entry2.place(anchor=E, relx=0.94, rely=0.41)
    label6 = Label(window2, text="Confirm Password:", font=("Arial Unicode MS", 16))
    label6.place(anchor=W, relx=0.06, rely=0.51)
    entry3 = Entry(window2, font=("Arial Unicode MS", 14), show="•", width=32)
    entry3.place(anchor=E, relx=0.94, rely=0.51)
    button2 = Button(window2, text="Change", command=onChangeButtonClicked, font=("Arial Unicode MS", 12), width=16, height=2)
    button2.place(anchor=E, relx=0.89, rely=0.66)
    window2.bind("<Return>", (lambda e, b=button2: b.invoke()))
    entry1.focus_set()
    window2.focus_force()
    window2.mainloop()
    
# Loads admin page
def adminPage():
    global window

    # Main Page: Event Listener
    def onLogOutButtonClicked():
        storage.logout()
        msg("Info", "Successfully logged out.")
        loginPage()
    def onEditButtonClicked():
        window.withdraw()
        studentEditor()
    def onEditPasswordButtonClicked():
        window.withdraw()
        editPasswordPage()


    window.withdraw()
    window = tkinter.Tk()
    window.title("School Management System")
    window.geometry("640x480")
    window.resizable(False, False)
    label1 = Label(window, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label3 = Label(window, text="Current user: admin", font=("Arial Unicode MS", 12))
    label3.place(anchor=W, relx=0.01, rely=0.21)
    button1 = Button(window, text="Log Out", command=onLogOutButtonClicked, font=("Arial Unicode MS", 8))
    button1.place(anchor=E, relx=0.99, rely=0.21)
    frame1 = Frame(window)
    frame1.place(anchor=N, relx=0.5, rely=0.31)
    button2 = Button(frame1, text="Create/edit student data", command=onEditButtonClicked, font=("Arial Unicode MS", 16))
    button2.grid(row=0, column=0, pady=3)
    button3 = Button(frame1, text="Edit password", command=onEditPasswordButtonClicked, font=("Arial Unicode MS", 16))
    button3.grid(row=3, column=0, pady=3)
    window.bind("<Return>", (lambda e: None))
    window.focus_force()
    window.mainloop()

# Loads student editor
def studentEditor():
    global window2

    # Student Editor: Event Listener
    def onLoadButtonClicked():
        sid = entry1.get()
        text2.delete(1.0, 52.0)
        try:
            text2.insert(END, storage.getRaw(sid))
        except IOError:
            if not checkID(sid):
                msg("Warning", "The student ID is incorrect.")
            storage.createID(sid, "", "", "")
    def onSaveButtonClicked():
        sid = entry1.get()
        storage.setLine(sid, text2.get(1.0, 2.0).split("\n")[0], line=1)
        for x in range(2, 53):
            storage.setLine(sid, text2.get(float(x), float(x + 1)).split("\n")[0], line=x)
        msg("Info", "The data has been modified.")
        button1.invoke()
    def onBackButtonClicked():
        window2.withdraw()
        adminPage()
    def onHelpButtonClicked():
        msg("Help", storage.getLinesHelp())

    window2 = tkinter.Tk()
    window2.title("Student Editor")
    window2.geometry("640x720")
    window2.resizable(False, False)
    label1 = Label(window2, text="Student ID:", font=("Arial Unicode MS", 12))
    label1.place(anchor=NW, relx=0.01, rely=0.01)
    entry1 = Entry(window2, font=("Arial Unicode MS", 12), width=32)
    entry1.place(anchor=NW, relx=0.16, rely=0.01)
    frame1 = Frame(window2)
    frame1.place(anchor=NE, relx=0.99, rely=0.01)
    button1 = Button(frame1, text="Load", command=onLoadButtonClicked, font=("Arial Unicode MS", 8))
    button1.grid(row=0, column=1, padx=3)
    button2 = Button(frame1, text="Save", command=onSaveButtonClicked, font=("Arial Unicode MS", 8))
    button2.grid(row=0, column=2, padx=3)
    button3 = Button(frame1, text="Back", command=onBackButtonClicked, font=("Arial Unicode MS", 8))
    button3.grid(row=0, column=3, padx=3)
    button4 = Button(frame1, text="Help", command=onHelpButtonClicked, font=("Arial Unicode MS", 8))
    button4.grid(row=0, column=0, padx=3)
    frame2 = Frame(window2)
    frame2.place(anchor=N, relx=0.5, rely=0.06)
    frame3 = Frame(frame2)
    frame3.pack(side=RIGHT, fill=Y)
    text1 = Text(frame2, height=52, width=4, font=("Arial Unicode MS", 7))
    text1.pack(side=LEFT, fill=Y)
    text1.insert(END, "1")
    for x in range(51):
        text1.insert(END, "\n" + str(x + 2))
    text2 = Text(frame3, height=52, width=96, font=("Arial Unicode MS", 7))
    text2.pack(side=LEFT, fill=Y)
    window2.bind("<Return>", (lambda e: None))
    entry1.focus_set()
    window2.focus_force()
    window2.mainloop()

# Loads edit password page
def editPasswordPage():
    global window2

    # Edit Password Page: Event Listener
    def onBackButtonClicked():
        window2.withdraw()
        adminPage()
    def onChangeButtonClicked():
        sid = entry0.get()
        oldPwd = entry1.get()
        newPwd = entry2.get()
        cPwd = entry3.get()
        if sid == "":
            sid = "admin"
            if newPwd != cPwd:
                msg("Warning", "Password and confirmed password are not identical.")
                window2.focus_force()
            elif newPwd == "" and cPwd == "":
                msg("Warning", "Please input your new password.")
                window2.focus_force()
            elif storage.changePassword(sid, oldPwd, newPwd) == 0:
                msg("Info", "Your password has been successfully changed.")
                onBackButtonClicked()
            else:
                msg("Warning", "Your old password is incorrect.")
                window2.focus_force()
        else:
            if newPwd != cPwd:
                msg("Warning", "Password and confirmed password are not identical.")
                window2.focus_force()
            elif newPwd == "" and cPwd == "":
                msg("Warning", "Please input your new password.")
                window2.focus_force()
            elif storage.changePassword(sid, oldPwd, newPwd, admin=True) == 0:
                msg("Info", "Your password has been successfully changed.")
                onBackButtonClicked()
            else:
                msg("Warning", "A runtime error ocured.")
                window2.focus_force()
        

    window2 = tkinter.Tk()
    window2.title("School Management System")
    window2.geometry("640x480")
    window2.resizable(False, False)
    label1 = Label(window2, text="Chung Ling High School", font=("Arial Bold", 24))
    label1.place(anchor=N, relx=0.5, rely=0.01)
    label2 = Label(window2, text="SCHOOL MANAGEMENT SYSTEM", font=("Arial", 16))
    label2.place(anchor=N, relx=0.5, rely=0.11)
    label0 = Label(window2, text="Current user: admin", font=("Arial Unicode MS", 12))
    label0.place(anchor=W, relx=0.01, rely=0.21)
    label3 = Label(window2, text="Student ID:", font=("Arial Unicode MS", 16))
    label3.place(anchor=W, relx=0.06, rely=0.31)
    entry0 = Entry(window2, font=("Arial Unicode MS", 14), width=32)
    entry0.place(anchor=E, relx=0.94, rely=0.31)
    button1 = Button(window2, text="Back", command=onBackButtonClicked, font=("Arial Unicode MS", 8))
    button1.place(anchor=E, relx=0.99, rely=0.21)
    label4 = Label(window2, text="Old Password:", font=("Arial Unicode MS", 16))
    label4.place(anchor=W, relx=0.06, rely=0.41)
    entry1 = Entry(window2, font=("Arial Unicode MS", 14), show="•", width=32)
    entry1.place(anchor=E, relx=0.94, rely=0.41)
    label5 = Label(window2, text="New Password:", font=("Arial Unicode MS", 16))
    label5.place(anchor=W, relx=0.06, rely=0.51)
    entry2 = Entry(window2, font=("Arial Unicode MS", 14), show="•", width=32)
    entry2.place(anchor=E, relx=0.94, rely=0.51)
    label6 = Label(window2, text="Confirm Password:", font=("Arial Unicode MS", 16))
    label6.place(anchor=W, relx=0.06, rely=0.61)
    entry3 = Entry(window2, font=("Arial Unicode MS", 14), show="•", width=32)
    entry3.place(anchor=E, relx=0.94, rely=0.61)
    button2 = Button(window2, text="Change", command=onChangeButtonClicked, font=("Arial Unicode MS", 12), width=16, height=2)
    button2.place(anchor=E, relx=0.89, rely=0.76)
    window2.bind("<Return>", (lambda e, b=button2: b.invoke()))
    entry0.focus_set()
    window2.focus_force()
    window2.mainloop()


# SCRIPT
storage.init("data/")
loginPage()
