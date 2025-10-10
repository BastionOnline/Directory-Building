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


jsonPath="path"

class Api:
    # load json file path
    def __init__(self, jsonPath="path"):
        self.jsonPath = jsonPath
    
    def selectFile(self):
        self.file_path = filedialog.askopenfilename(
            title="Choose a excel file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.file_path)
        return self.file_path

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



# Determine files and folders
FileName, FileNumber, Files, Cash_name, Sched_name, Sales_name, Invoice_name = files()
SourceDir, PrevDir, cwf, DestDir = folders()

PresentName, PresentSize, PresentDate, MissingName = propertyCheck(Files, SourceDir)


userIntro(MissingName, PresentName, Files, DestDir)

Userinput, year, yearpath, sourcepath, Answer, response = userCommand(DestDir, SourceDir)

# Date and ranges created
countdot, PeriodStart, TotalWeeks = customizeDate(year)

# Create files and configure them
numbermonths, YearDir = dirCreation(DestDir, year, Files, SourceDir, response)

# Makes Custom dates on file copies
excelCreator(numbermonths, FileName, YearDir, countdot, SourceDir, Files, PeriodStart, TotalWeeks)
