import webview
import os
import sys
import threading

from tkinter import filedialog
from modules.automation.templateSetup import initTemplate
from modules.automation import automation

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
        self.sourceDir = None
        self.files = None
        self.nameExcel = None
        self.nameSolo = None
        self.nameNumberedExcel = None
        self.window = None


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
        print(self.hotelFilePath)
        return self.hotelFilePath

    def selectDestinationFolder(self):
        self.destinationFolderPath = filedialog.askdirectory(
            title="Select a Folder For New Yearly Directory"
        )
        print(self.destinationFolderPath)
        return self.destinationFolderPath
    
    def dateSelection(self, dateInput):
        self.yearValue = dateInput

        print(self.yearValue)
        return self.yearValue
    
    def initializeBuildDirectory(self):
        def startThreading():
            self.sourceDir, self.files, self.nameExcel, self.nameSolo, self.nameNumberedExcel = initTemplate(self)

            DestDir = self.destinationFolderPath
            SourceDir = self.sourceDir
            FileName = self.nameSolo
            Files = self.nameNumberedExcel
            year = self.yearValue
            response = self.customizeDateBool

            automation(DestDir, SourceDir, FileName, Files, year, response, self)

        threading.Thread(target=startThreading, daemon=True).start()
        # Use daemon=True for background work like progress updates, file automation, etc., where it’s OK to stop when the app closes.
        # Use daemon=False if the task must complete before the program exits (e.g., saving files, database writes, etc.).

        return
        
# table for ui
# create progress bar
# change date input to year
# setup json
#     

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
    window = webview.create_window("Directory Builder", f"file://{html_file}", js_api=api)
    
    # Set the api self.window so python can push to it
    api.set_window(window)
    webview.start()

