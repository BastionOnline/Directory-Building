from datetime import date
import calendar
import os
import openpyxl
import shutil
from modules.statusUpdate import status

def dirCreation(DestDir, year, Files, SourceDir, response, self):
    ###################################################################################################################################
    #This formats xl

    def xlSales(inputdir, file, MY, FirstDay):

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

        print(SourceDir + "\\" + Files[4])
        print(HotelDir + "\\" + "Hotel - Schedule.xlsx")

        shutil.copyfile(SourceDir + "\\" + Files[4], HotelDir + "\\" + "Hotel - Schedule.xlsx")


    # Makes Month Dirs
    i = 0

    while i < 12:
        status(i, 11, "Directories created", self)

        MonthDir = os.path.join(YearDir, numbermonths[i])
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

            shutil.copyfile(SourceDir + "\\" + Files[2], SalesDir + "\\" + calendar.month_name[i+1] + " Monthly Sales.xlsx" )

            # Info for Sales update
            currentMY = monthabv[i] + " " + str(year)
            # print(currentMY)
            
            currentMon = date(year, int(i+1), 1)

            # if response == "yes":
            # if response == True:
            if response == "true":
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
        
    return numbermonths, YearDir

