from datetime import date
import calendar
import os
import openpyxl
import shutil
import win32com.client
from modules.statusUpdate import status
from modules.excelCustomize import xlSales
from modules.createDirectoryModule import createDir

def dirCreation(DestDir, year, Files, SourceDir, response, self):
    ###################################################################################################################################
    #This formats xl

    # def xlSales(inputdir, file, MY, FirstDay):

    #     print(f"starting ${file} config\n\n")
    #     print(f"inputdirectory:\n ${inputdir}")

    #     inputfile = os.path.join(inputdir, file)
    #     outputfile = os.path.join(inputdir, file)

    #     print("\nUpdating excel Sales file to " + MY + "...")

    #     workbook = openpyxl.load_workbook(inputfile)

    #     sheet = workbook['Yearly Calendar']
    #     cell = sheet['B2']
    #     cell.value = FirstDay

    #     workbook.save(outputfile)
    #     print("Sales file updated to " + MY + " and saved to\n" + outputfile)



    ###################################################################################################################################
    #This creates directories, make this section optional

    # Makes Year Dir
    months = calendar.month_name[1:]
    month_number = list(range(1,13))
    numbermonths = [f'{number}. {month}' for number, month in zip(month_number, months)]
    monthabv = [s[:3] for s in months]


    YearDir = os.path.join(DestDir, ("MTCC " + str(year)))
    

    if os.path.exists(YearDir):
        print("Year folder already exists")
    else:
        os.mkdir(YearDir)
        for t in Files:
            try:
                sourceFile = os.path.join(SourceDir, t)
                destinatonFile = os.path.join(YearDir,t)
                
                shutil.copyfile(sourceFile, destinatonFile)
            except:
                pass

    
    # Makes Hotel Dr
    HotelDir = os.path.join(YearDir,"Hotel")
    HotelFile = os.path.join(HotelDir, Files[4])

    sourceHotelFile = os.path.join(SourceDir, Files[4])
    destinationHotelFile = os.path.join(HotelDir, "Hotel - Schedule.xlsx")

    if os.path.exists(HotelDir):
        print("Hotel folder already exists")
        
        if os.path.exists(HotelFile):
            print("Hotel Schedule exists")
        else:
            shutil.copyfile(sourceHotelFile,  destinationHotelFile)
    else:
        os.mkdir(HotelDir)

        shutil.copyfile(sourceHotelFile,  destinationHotelFile)


    # def createDir(parentFolder, childFolder):
    #     directory = os.path.join(parentFolder, childFolder) 
    #     if os.path.exists(directory):
    #         print(f"{childFolder} folder already exists")
    #         return directory
    #     else:
    #         os.mkdir(directory)

    #         if (childFolder == "3. Sales"):
    #             salesPathSource = os.path.join(SourceDir, Files[2])
    #             salesPathDestination = os.path.join(directory, calendar.month_name[i+1] + " Monthly Sales.xlsx")

    #             shutil.copyfile(salesPathSource, salesPathDestination)

    #             # # Info for Sales update
    #             currentMY = monthabv[i] + " " + str(year)
    #             currentMon = date(year, int(i+1), 1)

    #             if response == "true":
    #                 xlSales(directory, calendar.month_name[i+1] + " Monthly Sales.xlsx", currentMY, currentMon)

    #         return directory


    # Makes Month Dirs
    i = 0
    while i < 12:
        status(i, 11, "Directories created", self)

        MonthDir = createDir(YearDir, numbermonths[i], SourceDir, Files, i, monthabv, year, response)
        EventDir = createDir(MonthDir, "1. Event Orders", SourceDir, Files, i, monthabv, year, response)
        ScheduleDir = createDir(MonthDir, "2. Schedules", SourceDir, Files, i, monthabv, year, response)
        SalesDir = createDir(MonthDir, "3. Sales", SourceDir, Files, i, monthabv, year, response)


        InvoiceDir = os.path.join(MonthDir, "4. Invoices")
        InSubDir = os.path.join(InvoiceDir, "Submitted")

        yearlyInvoicePath = os.path.join(YearDir, "4. Invoices.xlsx")
        monthlyInvoiceShortcutLink = os.path.join(InvoiceDir, "Invoices.lnk")


        def createShortcut(target, shortcut):
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortcut(shortcut)
            shortcut.TargetPath = target
            shortcut.Description = ""
            shortcut.WorkingDirectory = os.path.dirname(target)
            shortcut.save()

        target = yearlyInvoicePath
        shortcut = monthlyInvoiceShortcutLink


        if os.path.exists(InvoiceDir):
            print("4. Invoices folder already exists")

            if os.path.exists(InSubDir):
                print("Invoice Submitted folder already exists")
            else:
                os.mkdir(InSubDir)

                createShortcut(target, shortcut)

        else:
            os.mkdir(InvoiceDir)
            os.mkdir(InSubDir)

            createShortcut(target, shortcut)
    

        i += 1
        
    # i = 0
    # while i < 12:
    #     status(i, 11, "Customizing Sales", self)
    #     # Info for Sales update
    #     currentMY = monthabv[i] + " " + str(year)
    #     currentMon = date(year, int(i+1), 1)

    #     if response == "true":
    #         xlSales(SalesDir, calendar.month_name[i+1] + " Monthly Sales.xlsx", currentMY, currentMon)

    return numbermonths, YearDir