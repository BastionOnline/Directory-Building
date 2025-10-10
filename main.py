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
from modules.createDirectory import dirCreation

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

numbermonths, YearDir = dirCreation(DestDir, year, Files, SourceDir, response)


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

