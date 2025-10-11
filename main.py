import webview
import os
import sys
import shutil
from datetime import date, datetime

from tkinter import filedialog
from modules.fileSelect import files, folders
from modules.propCheck import propertyCheck
from modules.intro import userIntro
from modules.docCustomization import userCommand
from modules.dateCalculation import customizeDate
from modules.createDirectory import dirCreation
from modules.scheduleBuilder import excelCreator

fileGrouping = []

class Api:
    # load json file path
    def __init__(self):
        self.balanceFilePath = None
        self.scheduleFilePath = None
        self.salesFilePath = None
        self.invoiceFilePath = None
        self.hotelFilePath = None
        self.destinationFolderPath = None
        self.yearValue = None
        self.customizeDateBool = None

    def selectBalanceFile(self):
        self.balanceFilePath = filedialog.askopenfilename(
            title="Select a Balance file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.balanceFilePath)
        return self.balanceFilePath
    
    def selectScheduleFile(self):
        self.scheduleFilePath = filedialog.askopenfilename(
            title="Select a Schedule file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.scheduleFilePath)
        return self.scheduleFilePath
    
    def selectSalesFile(self):
        self.salesFilePath = filedialog.askopenfilename(
            title="Select a Sales file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.salesFilePath)
        return self.salesFilePath
    
    def customizeDate(self, bool):
        self.customizeDateBool = bool
        print(bool, type(bool))
        return self.customizeDateBool
    
    def selectInvoiceFile(self):
        self.invoiceFilePath = filedialog.askopenfilename(
            title="Select a Invoice file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.invoiceFilePath)
        return self.invoiceFilePath
    
    def selectHotelFile(self):
        self.hotelFilePath = filedialog.askopenfilename(
            title="Select a Hotel file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )

    def selectDestinationFolder(self):
        self.destinationFolderPath = filedialog.askdirectory(
            title="Select a Folder For New Yearly Directory"
        )
        print(self.destinationFolderPath)
        return self.destinationFolderPath
    
    def dateSelection(self, dateInput):
        dateObj = datetime.strptime(dateInput, "%Y-%m-%d")
        self.yearValue = dateObj.year

        print(self.yearValue)
        return self.yearValue
    
    def initializeBuildDirectory(self):
        # check if templates exist in current directory, if not, make one

        # check if files exist
        

        # make templates folder and copy files there
        fileGrouping.append([["Balance"], ["Balance.xlsx"], ["1. Balance.xlsx"], [self.balanceFilePath]])
        fileGrouping.append([["Schedules"], ["Schedules.xlsx"], ["2. Schedules.xlsx"], [self.scheduleFilePath]])
        # fileGrouping.append([["Sales"], ["Sales.xlsx"], ["3. Sales.xlsx"], [self.salesFilePath]])
        # fileGrouping.append([["Invoices"], ["Invoices.xlsx"], ["4. Invoices.xlsx"], [self.invoiceFilePath]])
        # fileGrouping.append([["Hotel - Schedule"], ["Hotel - Schedule.xlsx"], ["5. Hotel - Schedule.xlsx"], [self.hotelFilePath]])

        templatePath = os.getcwd() + "\\templates\\" + fileGrouping[1][2][0]
        os.path.exists(templatePath)
        samplePath = os.path.exists(self.balanceFilePath)

        # if templatePath & samplePath == True:
        #     print("nice")

        # print(templatePath)
        
        shutil.copyfile(self.balanceFilePath, templatePath)
        print("finished")
        
        # print(status, item)

        return
        
        

# need to initialize api before debugging

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# html_file = resource_path("index.html")
# css_file = resource_path("assets/style.css")
# js_file = resource_path("assets/script.js")


# enable for debugging
html_file = resource_path(r'.\frontend\index.html')
css_file = resource_path(r'.\frontend\assets\style.css')
js_file = resource_path(r'.\frontend\assets\script.js')


if __name__ == '__main__':
    # Example usage of transcribe function
    api = Api()

    # Open the HTML file in a webview window
    webview.create_window("Directory Builder", f"file://{html_file}", js_api=api)
    webview.start()


# print(api.yearValue)


# Determine files and folders
FileName, FileNumber, Files, Cash_name, Sched_name, Sales_name, Invoice_name = files()
SourceDir, PrevDir, cwf, DestDir = folders()

PresentName, PresentSize, PresentDate, MissingName = propertyCheck(Files, SourceDir)


userIntro(MissingName, PresentName, Files, DestDir)

Userinput, year, yearpath, sourcepath, Answer, response = userCommand(DestDir, SourceDir)

#Automation
# Date and ranges created
countdot, PeriodStart, TotalWeeks = customizeDate(year)

# Create files and configure them
numbermonths, YearDir = dirCreation(DestDir, year, Files, SourceDir, response)

# Makes Custom dates on file copies
excelCreator(numbermonths, FileName, YearDir, countdot, SourceDir, Files, PeriodStart, TotalWeeks)