from datetime import date
import calendar
import os
import openpyxl
import shutil
import win32com.client
from modules.statusUpdate import status

def dirCreation(DestDir, year, Files, SourceDir, response, self):
    ###################################################################################################################################
    #This formats xl

    def xlSales(inputdir, file, MY, FirstDay):

        print(f"starting ${file} config\n\n")
        print(f"inputdirectory:\n ${inputdir}")

        inputfile = os.path.join(inputdir, file)
        outputfile = os.path.join(inputdir, file)

        print("\nUpdating excel Sales file to " + MY + "...")

        workbook = openpyxl.load_workbook(inputfile)

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
                sourceFile = os.path.join(SourceDir, t)
                destinatonFile = os.path.join(YearDir,t)
                
                shutil.copyfile(sourceFile, destinatonFile)
                # shutil.copyfile(SourceDir + "\\" + t, YearDir + "\\" + t)
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
            # sourceHotelFile = os.path.join(SourceDir, Files[4])
            # destinationHotelFile = os.path.join(HotelDir, "Hotel - Schedule.xlsx")


            # shutil.copyfile(SourceDir + "\\" + Files[4],  HotelDir + "\\" + "Hotel - Schedule.xlsx")
    else:
        os.mkdir(HotelDir)

        shutil.copyfile(sourceHotelFile,  destinationHotelFile)
        # sourceHotelFile = os.path.join(SourceDir, Files[4])
        # destinationHotelFile = os.path.join(HotelDir, "Hotel - Schedule.xlsx")

        

        # print(SourceDir + "\\" + Files[4])
        # print(HotelDir + "\\" + "Hotel - Schedule.xlsx")

        # shutil.copyfile(SourceDir + "\\" + Files[4], HotelDir + "\\" + "Hotel - Schedule.xlsx")


    # Makes Month Dirs
    i = 0

    def createDir(parentFolder, childFolder):
        directory = os.path.join(parentFolder, childFolder) 
        if os.path.exists(directory):
            print(f"{childFolder} folder already exists")
            return directory
        else:
            os.mkdir(directory)

            if (childFolder == "3. Sales"):
                salesPathSource = os.path.join(SourceDir, Files[2])
                salesPathDestination = os.path.join(directory, calendar.month_name[i+1] + " Monthly Sales.xlsx")

                shutil.copyfile(salesPathSource, salesPathDestination)
                # shutil.copyfile(SourceDir + "\\" + Files[2], SalesDir + "\\" + calendar.month_name[i+1] + " Monthly Sales.xlsx" )

                # Info for Sales update
                currentMY = monthabv[i] + " " + str(year)
                currentMon = date(year, int(i+1), 1)

                if response == "true":
                    xlSales(directory, calendar.month_name[i+1] + " Monthly Sales.xlsx", currentMY, currentMon)


            return directory

    while i < 12:
        status(i, 11, "Directories created", self)

        MonthDir = createDir(YearDir, numbermonths[i])
        EventDir = createDir(MonthDir, "1. Event Orders")
        ScheduleDir = createDir(MonthDir, "2. Schedules")
        SalesDir = createDir(MonthDir, "3. Sales")

        # MonthDir = os.path.join(YearDir, numbermonths[i])
        # if os.path.exists(MonthDir):
        #     print(numbermonths[i] + " folder already exists")
        # else:
        #     os.mkdir(MonthDir)
        
        # EventDir = os.path.join(MonthDir, "1. Event Orders")
        # if os.path.exists(EventDir):
        #     print("1. Event Orders folder already exists")
        # else:
        #     os.mkdir(EventDir)

        # ScheduleDir = os.path.join(MonthDir, "2. Schedules")
        # if os.path.exists(ScheduleDir):
        #     print("2. Schedules folder already exists")
        # else:
        #     os.mkdir(ScheduleDir)

        SalesDir = os.path.join(MonthDir, "3. Sales")
        if os.path.exists(SalesDir):
            print("3. Sales folder already exists")
        else:
            os.mkdir(SalesDir)

            salesPathSource = os.path.join(SourceDir, Files[2])
            salesPathDestination = os.path.join(SalesDir, calendar.month_name[i+1] + " Monthly Sales.xlsx")

            shutil.copyfile(salesPathSource, salesPathDestination)
            # shutil.copyfile(SourceDir + "\\" + Files[2], SalesDir + "\\" + calendar.month_name[i+1] + " Monthly Sales.xlsx" )

            # Info for Sales update
            currentMY = monthabv[i] + " " + str(year)
            currentMon = date(year, int(i+1), 1)

            if response == "true":
                xlSales(SalesDir, calendar.month_name[i+1] + " Monthly Sales.xlsx", currentMY, currentMon)
                # NewSalesName = xlSales(SalesDir + "\\", calendar.month_name[i+1] + " Monthly Sales.xlsx", currentMY, currentMon)



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
        
    return numbermonths, YearDir

