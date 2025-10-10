import webview
import os
import sys
from tkinter import filedialog
from modules.fileSelect import files, folders
from modules.propCheck import propertyCheck
from modules.intro import userIntro
from modules.docCustomization import userCommand
from modules.dateCalculation import customizeDate
from modules.createDirectory import dirCreation
from modules.scheduleBuilder import excelCreator


class Api:
    # load json file path
    def __init__(self):
        self.balanceFilePath = None
        self.scheduleFilePath = None
        self.salesFilePath = None
        self.invoiceFilePath = None
    
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
            title="Select a Balance file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.salesFilePath)
        return self.salesFilePath
    
    def selectInvoiceFile(self):
        self.invoiceFilePath = filedialog.askopenfilename(
            title="Select a Balance file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.invoiceFilePath)
        return self.invoiceFilePath
    
    def selectDestinationFolder(self):
        self.destinationFolderPath = filedialog.askdirectory(
            title="Select a Folder"
        )
        print(self.invoiceFilePath)
        return self.invoiceFilePath

# need to initialize api before debugging
# api = Api(jsonPath)
# print(Api.loadUserDefaults(api, "whisper")) # returns true, debug looks in project folder, not src

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


path = api.balanceFilePath
print(path)


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
