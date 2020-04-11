# SCHOOL MANAGEMENT SYSTEM


# IMPORT LIBRARIES
import tkinter
from tkinter import messagebox
from os import system, name
import storage
import string


# GLOBAL VARIABLES
g_sid = ""
g_name = ""
g_class = ""
attempts = 3
        

# BASIC FUNCTIONS

# Clears the screen
def clear(): 
    if name == "nt": 
        _ = system("cls") 
    else: 
        _ = system("clear")

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

# Loads console
def loadConsole():
    global attempts
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("< Console Mode >")
    print("\nPlease input your credentials below. Type R in ID column to register for a new account.")
    sid = input("Student ID: ")
    if sid == "R":
        consoleCreateAccount()
                
    pwd = input("Password: ")
    if storage.login(sid, pwd) == 0:
        if sid != "admin":
            consoleMain(sid)
        consoleAdmin()
    elif storage.login(sid, pwd) == 1:
        attempts = attempts - 1
        if attempts <= 0:
            msg("Warning", "The system is closing due to 3 wrong attempts.")
            exit()
        msg("Warning", "The student ID doesn't exist. " + str(attempts) + " attempts left.")
        loadConsole()
    elif storage.login(sid, pwd) == 2:
        attempts = attempts - 1
        if attempts <= 0:
            msg("Warning", "The system is closing due to 3 wrong attempts.")
            exit()
        msg("Warning", "Your password is incorrect. " + str(attempts) + " attempts left.")
        loadConsole()

# Creates an account
def consoleCreateAccount():
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("< Console Mode >")
    print("\nCreate a new account\n")
    sid = input("Student ID: ")
    pwd = input("Password: ")
    cPwd = input("Confirm Password: ")
    name = input("Name: ")
    c = input("Class: ")
    if not checkID(sid):
        msg("Warning", "Your Student ID is incorrect.")
        consoleCreateAccount()
    elif not pwd == cPwd:
        msg("Warning", "Password and confirmed password are not identical.")
        consoleCreateAccount()
    elif pwd == "" and cPwd == "":
        msg("Warning", "Please input your password.")
        consoleCreateAccount()
    elif name == "":
        msg("Warning", "Please input your name.")
        consoleCreateAccount()
    elif c == "":
        msg("Warning", "Please input your class.")
        consoleCreateAccount()
    elif storage.createID(sid, pwd, name, c) == 0:
        print("\nYour account has been successfully created. Input anything to continue.")
        input("Input: ")
        loadConsole()
    else:
        msg("Warning", "Student already exists!")
    consoleCreateAccount()

# Creates an account manually (admin)
def consoleAdminCreateAccount():
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("< Console Mode >")
    print("\nCurrent User: admin")
    print("\nCreate account manually\n")
    print(storage.getLinesHelp())
    sid = input("\nStudent ID: ")
    if not checkID(sid):
        msg("Warning", "The Student ID is incorrect.")
        consoleAdminCreateAccount()
    data = []
    for x in range(52):
        data.append(input("Line " + str(x + 1) + ": "))
    for x in range(40):
        try:
            if int(data[x + 3]) < 0 or data[x + 3] == "":
                data[x + 3] = "0"
            elif int(data[x + 3]) > 100:
                data[x + 3] = "100"
        except:
            data[x + 3] == "0"
    if storage.createRaw(sid, data) == 0:
        print("\nThe account has been successfully created. Input anything to continue.")
        input("Input: ")
        consoleAdmin()
    else:
        msg("Warning", "A runtime error occured.")
        consoleAdminCreateAccount()

# Loads main page
def consoleMain(sid):
    global g_sid
    global g_name
    global g_class
    g_sid = sid
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("< Console Mode >")
    print("\nStudent Name: " + storage.getName())
    print("Class: " + storage.getClass())
    print("\nInput 1 to check exam result.")
    print("Input 2 to check cocurriculum info.")
    print("Input 3 to change password.")
    print("Input 0 to log out.")
    i = input("Input: ")
    if i == "0":
        storage.logout()
        msg("Info", "Successfully logged out.")
        loadConsole()
    elif i == "1":
        clear()
        print("CHUNG LING HIGH SCHOOL")
        print("SCHOOL MANAGEMENT SYSTEM")
        print("< Console Mode >")
        print("\nStudent Name: " + storage.getName())
        print("Class: " + storage.getClass())
        result = storage.getExamResult()
        print("\nUjian 1: \n")
        print("BC: " + result[0])
        print("BM: " + result[1])
        print("BI: " + result[2])
        print("MM: " + result[3])
        print("SC: " + result[4])
        print("ASK: " + result[5])
        print("SJ: " + result[6])
        print("GE: " + result[7])
        print("PM: " + result[8])
        print("\nPeperiksaan 1: \n")
        print("BC: " + result[9])
        print("BM: " + result[10])
        print("BI: " + result[11])
        print("MM: " + result[12])
        print("SC: " + result[13])
        print("ASK: " + result[14])
        print("SJ: " + result[15])
        print("GE: " + result[16])
        print("PM: " + result[17])
        print("PJK: " + result[18])
        print("PSV: " + result[19])
        print("\nUjian 2: \n")
        print("BC: " + result[20])
        print("BM: " + result[21])
        print("BI: " + result[22])
        print("MM: " + result[23])
        print("SC: " + result[24])
        print("ASK: " + result[25])
        print("SJ: " + result[26])
        print("GE: " + result[27])
        print("PM: " + result[28])
        print("\nPeperiksaan 2: \n")
        print("BC: " + result[29])
        print("BM: " + result[30])
        print("BI: " + result[31])
        print("MM: " + result[32])
        print("SC: " + result[33])
        print("ASK: " + result[34])
        print("SJ: " + result[35])
        print("GE: " + result[36])
        print("PM: " + result[37])
        print("PJK: " + result[38])
        print("PSV: " + result[39])
        print("\nInput anything to continue.")
        input("Input: ")
        consoleMain(sid)
    elif i == "2":
        clear()
        print("CHUNG LING HIGH SCHOOL")
        print("SCHOOL MANAGEMENT SYSTEM")
        print("< Console Mode ?")
        print("\nStudent Name: " + storage.getName())
        print("Class: " + storage.getClass())
        co = storage.getCocurriculum()
        print("\nName: " + co[0])
        print("Category: Pakaian Beruniform")
        print("Pose: " + co[1])
        print("Marks: " + co[2])
        print("\nName: " + co[3])
        print("Category: Persatuan")
        print("Pose: " + co[4])
        print("Marks: " + co[5])
        print("\nName: " + co[6])
        print("Category: Sukan / Permainan")
        print("Pose: " + co[7])
        print("Marks: " + co[8])
        print("\nInput anything to continue.")
        input("Input: ")
        consoleMain(sid)
    elif i == "3":
        consoleChangePassword()
    else:
        msg("Warning", "Please enter a correct input.")
        consoleMain(sid)

# Changes password
def consoleChangePassword():
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("< Console Mode >")
    print("\nStudent Name: " + storage.getName())
    print("Class: " + storage.getClass())
    print("\nChange password\n")
    oldPwd = input("Old Password: ")
    newPwd = input("New Password: ")
    cPwd = input("Confirm Password: ")
    if newPwd != cPwd:
        msg("Warning", "Password and confirmed password are not identical.")
        consoleChangePassword()
    elif newPwd == "" and cPwd == "":
        msg("Warning", "Please input your new password.")
        consoleChangePassword()
    elif storage.changePassword(g_sid, oldPwd, newPwd) == 0:
        print("\nYour password has been successfully changed. Input anything to continue.")
        input("Input: ")
        consoleMain(g_sid)
    else:
        msg("Warning", "Your old password is incorrect.")
        consoleChangePassword()

# Changes password (admin)
def consoleAdminChangePassword():
    global g_sid
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("< Console Mode >")
    print("\nCurrent User: admin")
    print("\nChange password\n")
    sid = input("Student ID (leave blank to change admin password): ")
    oldPwd = input("Old Password (only required to change admin password): ")
    newPwd = input("New Password: ")
    cPwd = input("Confirm Password: ")
    if sid == "":
        if newPwd != cPwd:
            msg("Warning", "Password and confirmed password are not identical.")
            consoleAdminChangePassword()
        elif newPwd == "" and cPwd == "":
            msg("Warning", "Please input your new password.")
            consoleAdminChangePassword()
        elif storage.changePassword(g_sid, oldPwd, newPwd) == 0:
            print("\nYour password has been successfully changed. Input anything to continue.")
            input("Input: ")
            consoleAdmin()
        else:
            msg("Warning", "Your old password is incorrect.")
            consoleAdminChangePassword()
    else:
        if not checkID(sid):
            msg("Warning", "The Student ID is incorrect.")
            consoleAdminChangePassword()
        if newPwd == "" and cPwd == "":
            msg("Warning", "Please input the new password.")
            consoleAdminChangePassword()
        elif storage.changePassword(sid, oldPwd, newPwd, admin=True) == 0:
            print("\nThe password has been successfully changed. Input anything to continue.")
            input("Input: ")
            consoleAdmin()
        else:
            msg("Warning", "A runtime error occured.")
            consoleAdminChangePassword()

# Modifies student data
def consoleAdminModifyData():
    global g_sid
    global g_name
    global g_class
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("< Console Mode >")
    print("\nCurrent User: admin")
    print("\nModify student data")
    sid = input("\nStudent ID: ")
    if not checkID(sid):
        msg("Warning", "The Student ID is incorrect.")
        consoleAdminModifyData()
    consoleAdminRewriteLine(sid)

# Rewrites student data
def consoleAdminRewriteLine(sid):
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("< Console Mode >")
    print("\nCurrent User: admin")
    print("\nModify student data: " + str(sid) + "\n")
    print(storage.getLinesHelp())
    print("\nInput line number to edit. Input 0 to exit.\n")
    line = int(input("Line: "))
    if line == 0:
        consoleAdmin()
    print("Original Data: " + storage.getLine(sid, line=line))
    data = input("New Data: ")
    if line >= 4 and line <= 43:
        try:
            if int(data) < 0 or data == "":
                data = "0"
            elif int(data) > 100:
                data = "100"
        except:
            data = "0"
    if storage.setLine(sid, data, line=line) == 0:
        msg("Info", "The data has been modified.")
    else:
        msg("Warning", "A runtime error occured.")
    consoleAdminRewriteLine(sid)

# Loads main page (admin)
def consoleAdmin():
    global g_sid
    global g_name
    global g_class
    g_sid = "admin"
    g_name = "admin"
    g_class = "admin"
    clear()
    print("CHUNG LING HIGH SCHOOL")
    print("SCHOOL MANAGEMENT SYSTEM")
    print("< Console Mode >")
    print("\nCurrent User: admin")
    print("\nInput 1 to manually create student data file (with 52 lines).")
    print("Input 2 to modify student data by line.")
    print("Input 3 to change password (including yours).")
    print("Input 0 to log out.")
    i = input("Input: ")
    if i == "0":
        storage.logout()
        msg("Info", "Successfully logged out.")
        loadConsole()
    elif i == "1":
        consoleAdminCreateAccount()
    elif i == "2":
        consoleAdminModifyData()
    elif i == "3":
        consoleAdminChangePassword()
    else:
        msg("Warning", "Please enter a correct input.")
        consoleAdmin()


# SCRIPT

storage.init("data/")
loadConsole()
