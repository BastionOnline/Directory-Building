from datetime import date, timedelta
import openpyxl
import shutil
import calendar
import os
from modules.fileSelect import files, folders
from modules.propCheck import propertyCheck
from modules.intro import userIntro
from modules.docCustomization import userCommand
from modules.dateCalculation import customizeDate

FileName, FileNumber, Files, Cash_name, Sched_name, Sales_name, Invoice_name = files()
SourceDir, PrevDir, cwf, DestDir = folders()

PresentName, PresentSize, PresentDate, MissingName = propertyCheck(Files, SourceDir)

##########################################################################################################################
#Code to Exit Program

##########################################################################################################################

userIntro(MissingName, PresentName, Files, DestDir)
      
##########################################################################################################################

Userinput, year, yearpath, sourcepath, Answer, response = userCommand(DestDir, SourceDir)

##########################################################################################################################

countdot, PeriodStart, TotalWeeks = customizeDate(year)

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

