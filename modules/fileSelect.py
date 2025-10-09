import os

##########################################################################################################################
#THIS IS FOR DIRECTORY SETUP
def files():
    FileName = ["Cash - Balance", "Schedules", "Sales", "Invoices"]
    FileNumber = range(6)
    # for FileNumber in FileNumber:
    #     print(FileNumber)
    Files = ["1. Cash - Balance.xlsx", "2. Schedules.xlsx", "3. Sales.xlsx", "4. Invoices.xlsx", "5. Hotel - Schedule.xlsx", "6. Monthly DB Builder.exe", "7. DB Reader.exe", "8. Yearly DB Builder.exe"]

    # for t in Files:
    #     print(t)

    # file_name = input("What is the file name? \n")
    # file_ext = input("What is the file extenstion? \n.")
    # Name_Ext = (file_name + "." + file_ext)

    #Name_Ext = "WIY.xlsx"

    Cash_name = Files[0]
    Sched_name = Files[1]
    Sales_name = Files[2]
    Invoice_name = Files[3]


    # Sched_name = "2. Schedules"
    # Invoice_name = "4. Invoices"

    # Invoice_name = input("What is the name of the invoice? ")
    # Sched_name = input("What is the name of the Schedule? ")


    return FileName, FileNumber, Files, Cash_name, Sched_name, Sales_name, Invoice_name

def folders():
    #SourceDir = 'C:\\My Stuff\\work\\coding projects\\'
    # # Dest_Main = 'C:\\My Stuff\\work\\coding projects\\November\\'
    # # Dest_Temp = 'C:\\My Stuff\\work\\coding projects\\owstuff\\'
    # # Dest_Yearly = 'C:\\My Stuff\\work\\coding projects\\Nowstuff\\'
    #DestTest = 'C:\\My Stuff\\work\\coding projects\\Nowstuff\\'



    # current = os.getcwd()

    # print(os.path.split(current))

    # root, work = os.path.split(current)

    # print("This is root " + root)
    # print("This is work " + work)


    SourceDir = os.getcwd() + "\\"
    print(SourceDir)
    # PrevDir, cwf = os.path.split(SourceDir)
    # Can't use this phrasing because of the extra line in 47 given
    # when using os.getcwd(), it looks for the slash as a terminating point, os it results in a blank folder
    # example, line 47 has \\, it's read as cwd\blank\, spliting this would just make cwd\.
    # so it did "split" a the folder, but based on slashes


    PrevDir, cwf = os.path.split(os.getcwd())
    # print(SourceDir + " is the source dir")
    # print(PrevDir + " is the previous dir")
    # print(cwf + " is the current folder")


    DestDir = PrevDir + "\\"

    # SourceDir = input("What are these files located? For example C:\\..") + "\\"
    # DestTest = input("Where do you want the yearly folder? This will be the folder that say 2024 for example") + "\\"

    # for 
    # shutil.copyfile(SourceDir + Name_Ext, ")

    #this uses the calendar mod
    #1: is used to omit the first string which is empty
    return SourceDir, PrevDir, cwf, DestDir