import os
import calendar
import shutil
from datetime import date
from modules.excelCustomize import xlSales

def createDir(parentFolder, childFolder, SourceDir, Files, i, monthabv, year, response):
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

                # # Info for Sales update
                currentMY = monthabv[i] + " " + str(year)
                currentMon = date(year, int(i+1), 1)

                if response == "true":
                    xlSales(directory, calendar.month_name[i+1] + " Monthly Sales.xlsx", currentMY, currentMon)

            return directory