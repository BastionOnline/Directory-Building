import openpyxl
from datetime import timedelta
import os
import shutil
from modules.statusUpdate import status

def excelCreator(numbermonths, FileName, YearDir, countdot, SourceDir, Files, PeriodStart, TotalWeeks):
    
    # Schedule Adjustment
    def ShedUpdate(FileDir, File, MY):

        #this will print month and day without leading 0's, ie. Feb 4, %e did not work, left a space in its' place
        MonYear = MY.strftime('%b %#d')
        ExcelDateFormat =  MY.strftime('%#m/%#d/%Y')

        print("Updating excel " + File + " to " + MonYear + "...")

        workbook = openpyxl.load_workbook(FileDir)

        sheet = workbook['Yearly Calendar']
        cell = sheet['B2']
        cell.value = MY


        workbook.save(FileDir)
        print("Sales file updated to " + MonYear + " and saved to\n" + FileDir)



    # Create custom files
    def createFile(PeriodStart, TotalWeeks, FileNumber):
        period = 0

        while period < TotalWeeks:
            status(period, TotalWeeks-1, "Schedules created")
            #print("period is", period, "Count is", count)
            CurWeek = PeriodStart + timedelta(weeks=period)
            EndWeek = CurWeek + timedelta(days=6)
            print(CurWeek)

            EndMInt = int(EndWeek.strftime('%m'))
            #prints the day value

            # location = 1. january > 1. Cash - Balances
            MInShedFold = os.path.join(numbermonths[EndMInt-1], str(FileNumber+1) + ". " + FileName[FileNumber])
            print(MInShedFold)
            
            InSchedDir = os.path.join(YearDir, MInShedFold)
            print(InSchedDir)
            
            DraftDir = os.path.join(InSchedDir, "Draft")
            FileDir = InSchedDir + "\\" + countdot[period] + " - " + FileName[FileNumber] + ".xlsx"
            SourceFile = os.path.join(SourceDir, str(Files[FileNumber]))
            print(SourceFile)
            # SourceFile = SourceDir + str(Files[FileNumber])

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


    createFile(PeriodStart, TotalWeeks, 1)