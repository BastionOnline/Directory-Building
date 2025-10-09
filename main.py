from datetime import date, timedelta
import openpyxl
import shutil
import calendar
import os
from modules.greeting import hello
from modules.fileSelect import files, folders

FileName, FileNumber, Files, Cash_name, Sched_name, Sales_name, Invoice_name = files()
SourceDir, PrevDir, cwf, DestDir = folders()

##########################################################################################################################
# THIS CHECKS FILE PROPERTIES

# FSizes = []
PresentName = []
PresentSize = []
PresentDate = []
MissingName = []

def Attributes():
    
    f = 0

    for f in range(len(Files)):

        filecheck = os.path.exists(SourceDir + Files[f])

        if filecheck == False:
            MissingName.append(Files[f])
            # print(Files[f] + " was not found")
            f +=1

        else:
            # print(Files[f] + " located")
            PresentName.append(Files[f])
            PresentSize.append(os.path.getsize(Files[f]))
            PresentDate.append(os.path.getctime(Files[f]))
            # FSizes.append(SourceDir + Files[f])
            f +=1

    # print(len(PresentName))

Attributes()

##########################################################################################################################
#Code to Exit Program

ClosePhrase =["stop", "exit", "close", "end"]

def CloseProgram(Exitcmd):

    for x in ClosePhrase:
    # This loop returns a VALUE not an index, so compare directly
        if Exitcmd.lower() == x:
            # print(x.capitalize() + "ing program")
            ## exit() raise the SystemExit exception so can code this in that block
            exit()
            #sys.exit()
            #Sys.exit, EXITS IMMEDIATELY!
                #still showed returning to code block, so will just use reg exit
        # else:
            #else statements do NOT need to be present all the time
    return Exitcmd



    # for x in ClosePhrase:

    #     if Exitcmd == ClosePhrase[x]:
    #         print(ClosePhrase[x] + "ing program")
    #         exit()
    #     else:
    #         return Exitcmd


#     if Exitcmd == "exit":
#         print("Exiting program")
#         exit()
# #        return None
#     else:
#         return Exitcmd

    # c = 0
    
    # while c < len(ClosePhrase):
    #     if Exitcmd.lower() == ClosePhrase[c]:
    #         print(ClosePhrase[c] + "ing program.")
    #         return None
    #     elif c == 0:
    #         c +=1
    #     else:
    #         return Exitcmd

##########################################################################################################################

print("\nThis is a directory building program.")
print("If you want to stop this program, type stop or exit, or press 'CTRL' + 'C' at any time\n")

if len(MissingName) == 0:
    
    for Templates in Files:
        print(Templates + " is ready to copy.")
    
    print("\nAll files needed to build this directory are present.\n")

else:
    
    if len(PresentName) == 0:
        print("\n*** NO FILES ARE IN " + os.getcwd() + " ***\n")
    else:
        print("The following are present:")
        for Templates in PresentName:
            print(Templates)

    print("\nThe following are NOT present in this folder and WILL NOT be created in the directory:")

    for Missing in MissingName:
        print(Missing)

    print("\nPlease place these missing files in " + os.getcwd())

# print("The current directory is:\n" + os.getcwd() + "\n")
print("\nThe Destination Directory is:\n" + DestDir + "\n\n")
# print("Please make sure the following files are in this folder:")

# f = 0
# while f <= 3:
#     print(Files[f] + "\n")
#     f +=1
      

while True:
    try:
        Userinput = input("What year do you want to create? ")

        CloseProgram(Userinput)

        year = int(Userinput)
        yearpath = os.path.join(DestDir,"MTCC " + Userinput)
        sourcepath = os.path.join(SourceDir,"MTCC " + Userinput)
        # print(sourcepath)

        if year < 0:
            print("This is not a valid year")
        elif year < 2000:
            print("Please enter a later year")
        # elif year > 2050:
        #     print("Please enter a earlier year")
        elif os.path.exists(yearpath):
            print("Year already exists")
        else:
            break
    except ValueError:
        print("This is not a year")
    # except SystemExit:
    #     print(Userinput.capitalize() + "ing program")
    # THIS WILL CYCLE BACK LOOP
    # CAN JUST USE SYS.EXIT TO EXIT IMMEDIATELY


while True:
    Answer = input("\nDo you want the Sales documents dates automatically set?\nThis will take a bit of additional time to complete, about 20 seconds per file, approximately 5 minutes total.\nPlease type either yes or no\n\n")
    response = Answer.lower()

    if response == "no":
        print("Sales documents dates will not be automatically set.\n")
        break
    elif response == "yes":
        print("Sales documents dates will be automatically set.\n")
        break
    else:
        print("\nPlease respond with yes or no.\n")

# while True:
#     year = int(input("What year do you want to create? "))
#     if NameError(year):
#         year = int(input("Please enter valid year"))
#     elif ValueError(year):
#         year = int(input("Please enter a valid year"))
#     print("Invalid.")

    
#month = int(input("What month do you want to start from? "))


# while year < 0:


# date(year, month, day)
d = date(year, 1, 1)

#d = date(year, month, 1)
# d = date(2018, 10, 1)

#Finds the beginning of the work period, monday, of the work year
def PStart(MonthStart):
    weekday = int(MonthStart.strftime('%u'))
    Monday = MonthStart - timedelta(days=(weekday-1))
    #print("The start day is", Monday.strftime('%a %b %Y'))
    return Monday

#finds the ending of the work period, sunday, of the the work year
def PEnd(Monday):
    Sun = Monday + timedelta(days=6)
    return Sun

PeriodStart = PStart(d)
PeriodEnd = PEnd(PeriodStart)

#determines the months being produced
SMonthNum = int(PeriodStart.strftime('%m'))
EMonthNum = int(PeriodEnd.strftime('%m'))

#find weeks in a month
def TotWeeks(intial, FirstMonday):
    EndYear = int(intial.strftime('%Y')) + 1
    
    Weeks = 0
    CurrentYear = 0

    while CurrentYear < EndYear:
        NxtWeek = FirstMonday + timedelta(weeks=Weeks)
        CurrentYear = int(NxtWeek.strftime('%Y'))
        if CurrentYear < EndYear:
            Weeks += 1
        else:
            #print(NxtWeek)
            return Weeks-1

TotalWeeks = TotWeeks(d, PeriodStart)
#print(TotalWeeks)


Startingdays = []

#loads array with dates
def PeriodsInYear(PeriodStart, TotalWeeks):
    period = 0
    
    while period < TotalWeeks:
        CurWeek = PeriodStart + timedelta(weeks=period)
        EndWeek = CurWeek + timedelta(days=6)
        
        #print(CurWeek)
        
        StartMonth = int(CurWeek.strftime('%m'))
        EndMonth = int(EndWeek.strftime('%m'))
        
        if StartMonth == EndMonth:
            comb = CurWeek.strftime('%b'), CurWeek.strftime('%#d'), EndWeek.strftime('%#d'), ",",  EndWeek.strftime('%Y')
            Startingdays.append(comb)
            #print("equal", StartMonth, EndMonth)
        else:
            comb2 = CurWeek.strftime('%b'), CurWeek.strftime('%#d'), EndWeek.strftime('%b %#d'), ",", EndWeek.strftime('%Y')
            Startingdays.append(comb2)
            #print("not equal", StartMonth, EndMonth)

        period +=1
        #print(period, "/", TotalWeeks, "\n")
        continue

 
PeriodsInYear(PeriodStart, TotalWeeks)

formatted_strings = [''.join([entry[0]," ", str(entry[1]), "-", str(entry[2]), str(entry[3]), " ", str(entry[4])]) for entry in Startingdays]
#print(formatted_strings)


# for formatted_strings in formatted_strings:
#     print(formatted_strings)

MonthlyCounter = []

#finds number of week in month
def WeekNumber(PeriodStart, TotalWeeks):
    period = 0
    count = 0

    while period < TotalWeeks:
        #print("period is", period, "Count is", count)
        CurWeek = PeriodStart + timedelta(weeks=period)
        EndWeek = CurWeek + timedelta(days=6)
        
        #print(CurWeek)
        CurMInt = int(CurWeek.strftime('%m'))
        EndMInt = int(EndWeek.strftime('%m'))
        #prints the day value
        Weekday = int(CurWeek.strftime('%d'))

        #print(Weekday)
        
        #if the start of the period 1, it has to be the first in the list
        if Weekday == 1:
            count =1
            period +=1
            #print("period is", period, "Count is", count, "\n")
            MonthlyCounter.append(count)
        
        #if the current week month matches ending week month keep counting
        elif CurMInt == EndMInt:
            count +=1
            period +=1
            #print("period is", period, "Count is", count, "\n")
            MonthlyCounter.append(count)

        #if the month changes start from the beginning
        else:
            count=1
            period +=1
            #print("period is", period, "Count is", count, "\n")
            MonthlyCounter.append(count)
            continue

WeekNumber(PeriodStart, TotalWeeks)

# for MonthlyCounter in MonthlyCounter:
    # print(MonthlyCounter)    

NumPeriod = []

countdot = [f'{number}. {item}' for number, item in zip(MonthlyCounter, formatted_strings)]

# for countdot in countdot:
#     print(countdot)    

###################################################################################################################################
#This formats xl

def xlSales(inputdir, file, MY, FirstDay):

    inputfile = os.path.join(inputdir, file)
    outputfile = os.path.join(inputdir, file)

    print("\nUpdating excel Sales file to " + MY + "...")

    workbook = openpyxl.load_workbook(inputfile)
    # shutil.copy("C:/My Stuff/work/coding projects/Small Projects/3. Sales.xlsx", "C:/My Stuff/work/coding projects/Small Projects/3. Sales-test.xlsx")

    sheet = workbook['Yearly Calendar']
    cell = sheet['B2']
    cell.value = FirstDay

    workbook.save(outputfile)
    print("Sales file updated to " + MY + " and saved to\n" + outputfile)



###################################################################################################################################
#This creates directories, make this section optional

# Makes Year Dir
months = calendar.month_name[1:]
month_number = list(range(1,13))
numbermonths = [f'{number}. {month}' for number, month in zip(month_number, months)]
monthabv = [s[:3] for s in months]


YearDir = os.path.join(DestDir, ("MTCC " + str(year)))
#print(YearDir)

if os.path.exists(YearDir):
    print("Year folder already exists")
else:
    os.mkdir(YearDir)
    for t in Files:
        try:
            shutil.copyfile(SourceDir + "\\" + t, YearDir + "\\" + t)
        except:
            pass

# Makes Yearly DB
# shutil.copyfile(SourceDir + "\\" + Files[6], YearDir + "\\" + "DB Builder.exe")



# Makes Hotel Dr
HotelDir = os.path.join(YearDir,"Hotel")
HotelFile = os.path.join(HotelDir, Files[4])
if os.path.exists(HotelDir):
    print("Hotel folder already exists")
    
    if os.path.exists(HotelFile):
        print("Hotel Schedule exists")
    else:
        shutil.copyfile(SourceDir + "\\" + Files[4],  HotelDir + "\\" + "Hotel - Schedule.xlsx")
else:
    os.mkdir(HotelDir)
    shutil.copyfile(SourceDir + "\\" + Files[4], HotelDir + "\\" + "Hotel - Schedule.xlsx")


# Makes Month Dirs
i = 0

while i < 12:
    MonthDir = os.path.join(YearDir, numbermonths[i])
    # print(MonthDir)
    
    if os.path.exists(MonthDir):
        print(numbermonths[i] + " folder already exists")
    else:
        os.mkdir(MonthDir)
       
    EventDir = os.path.join(MonthDir, "1. Event Orders")
    if os.path.exists(EventDir):
        print("1. Event Orders folder already exists")
    else:
        os.mkdir(EventDir)

    ScheduleDir = os.path.join(MonthDir, "2. Schedules")
    if os.path.exists(ScheduleDir):
        print("2. Schedules folder already exists")
    else:
        os.mkdir(ScheduleDir)

    SalesDir = os.path.join(MonthDir, "3. Sales")
    if os.path.exists(SalesDir):
        print("3. Sales folder already exists")
    else:
        os.mkdir(SalesDir)

        # print("sources: " + os.getcwd() + Files[2])
        # print("Destination: " + MonthDir + calendar.month_name[i+1] + " Sales.xlsx" )

        # print(SourceDir + "\\" + Files[2])
        # print(SalesDir + "\\" + calendar.month_name[i+1] + " Monthly Sales.xlsx")
        shutil.copyfile(SourceDir + "\\" + Files[2], SalesDir + "\\" + calendar.month_name[i+1] + " Monthly Sales.xlsx" )

        # DB Builder program
        shutil.copyfile(SourceDir + "\\" + Files[5], SalesDir + "\\" + "1. DB Builder.exe")
        shutil.copyfile(SourceDir + "\\" + Files[6], SalesDir + "\\" + "2. DB Reader.exe")


        # Info for Sales update
        currentMY = monthabv[i] + " " + str(year)
        # print(currentMY)
        
        currentMon = date(year, int(i+1), 1)

        if response == "yes":
            NewSalesName = xlSales(SalesDir + "\\", calendar.month_name[i+1] + " Monthly Sales.xlsx", currentMY, currentMon)

    InvoiceDir = os.path.join(MonthDir, "4. Invoices")
    InSubDir = os.path.join(InvoiceDir, "Submitted")
    if os.path.exists(InvoiceDir):
        print("4. Invoices folder already exists")

        if os.path.exists(InSubDir):
            print("Invoice Submitted folder already exists")
        else:
            os.mkdir(InSubDir)
    else:
        os.mkdir(InvoiceDir)
        os.mkdir(InSubDir)
        

    i += 1
    


#####################################################################################################################################

# Schedule Adjustment

def ShedUpdate(FileDir, File, MY):

    #this will print month and day without leading 0's, ie. Feb 4, %e did not work, left a space in its' place
    MonYear = MY.strftime('%b %#d')
    ExcelDateFormat =  MY.strftime('%#m/%#d/%Y')

    print("Updating excel " + File + " to " + MonYear + "...")

    workbook = openpyxl.load_workbook(FileDir)
    # shutil.copy("C:/My Stuff/work/coding projects/Small Projects/3. Sales.xlsx", "C:/My Stuff/work/coding projects/Small Projects/3. Sales-test.xlsx")

    sheet = workbook['Yearly Calendar']
    cell = sheet['B2']
    cell.value = MY


    workbook.save(FileDir)
    print("Sales file updated to " + MonYear + " and saved to\n" + FileDir)

#####################################################################################################################################

# UPDATING PORTION


def Move(PeriodStart, TotalWeeks, FileNumber):
    period = 0

    while period < TotalWeeks:
        #print("period is", period, "Count is", count)
        CurWeek = PeriodStart + timedelta(weeks=period)
        EndWeek = CurWeek + timedelta(days=6)
        print(CurWeek)

        EndMInt = int(EndWeek.strftime('%m'))
        #prints the day value


        # finaldest = numbermonths[EndMInt-1] + "\\" + FileNumber + ". " + FileName[FileNumber]
        # finaldest = numbermonths[EndMInt-1] + "\\4. Invoices\\"
        
        # location = 1. january > 1. Cash - Balances
        MInShedFold = os.path.join(numbermonths[EndMInt-1], str(FileNumber+1) + ". " + FileName[FileNumber])
        print(MInShedFold)
        
        InSchedDir = os.path.join(YearDir, MInShedFold)
        print(InSchedDir)
        
        DraftDir = os.path.join(InSchedDir, "Draft")
        FileDir = InSchedDir + "\\" + countdot[period] + " - " + FileName[FileNumber] + ".xlsx"
        SourceFile = SourceDir + str(Files[FileNumber])

        if os.path.exists(FileDir):
            print(FileDir + " already exists.\n File moved to Draft folder. \n\n")
            
            if os.path.exists(DraftDir):
                print("Draft folder already exists.")
            else:
                os.mkdir(DraftDir)
                print(DraftDir + " directory made.")

            shutil.move(FileDir, DraftDir)
            print("file moved to" + DraftDir)
            
            shutil.copyfile(SourceFile, FileDir)
            print("Source file: " + SourceFile)
            print(FileDir + " created.")

            if FileNumber == 1:
                
                ShedUpdate(FileDir, countdot[period] + " - " + FileName[FileNumber] + ".xlsx", CurWeek)
                period +=1
            else:
                period +=1

        else:
            shutil.copyfile(SourceFile, FileDir)
            print("Source file: " + SourceFile)
            print(FileDir + " created.")

            if FileNumber == 1:
                
                ShedUpdate(FileDir, countdot[period] + " - " + FileName[FileNumber] + ".xlsx", CurWeek)
                period +=1
            else:
                period +=1



Move(PeriodStart, TotalWeeks, 1)
Move(PeriodStart, TotalWeeks, 3)

