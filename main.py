import json
import webview
import os
import sys
import threading

from tkinter import filedialog, messagebox
from modules.templateSetup import initTemplate
from modules.initAuto import automation
from modules.statusUpdate import status

# load json file path

templateFolderDir = os.path.join(os.getcwd(), "templates")

jsonPath = "./userDefaults.json"

jsonFile = os.path.join(templateFolderDir,jsonPath)
print(jsonFile)

print(os.path.exists(templateFolderDir))
templateFolderStat = os.path.exists(templateFolderDir)


def setDefault(key, value, jsonPath=jsonFile):
    try:
        with open(jsonPath, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # Update the dictionary
    data[key] = value

    # Write the updated data back to the file (pretty format)
    with open(jsonPath, "w") as f:
        json.dump(data, f, indent=4)
    return


def createJson():
    if templateFolderStat == False:
        os.mkdir(templateFolderDir)


    print(os.path.exists(jsonFile))
    if os.path.exists(jsonFile) == False:
        data = {
            "Year": "",
            "Customize Date": "true",
            "Balance": "",
            "Schedules": "",
            "Sales": "",
            "Invoices": "",
            "Hotel - Schedule": "",
            "Destination Folder": ""
        }

        with open(jsonFile, "w") as f:
            json.dump(data, f, indent=4)  
    return

createJson()

def updateJsonExcel():
    presentExcelFiles = [
                            [["Balance"], ["1. Balance.xlsx"]],
                            [["Schedules"], ["2. Schedules.xlsx"]],
                            [["Sales"], ["3. Sales.xlsx"]],
                            [["Invoices"], ["4. Invoices.xlsx"]],
                            [["Hotel - Schedule"], ["5. Hotel - Schedule.xlsx"]]
                        ]

    # check if files exist in template folder
    for file in presentExcelFiles:
        filePath = os.path.join(templateFolderDir, file[1][0])
        if os.path.exists(filePath) == True:
            setDefault(file[0][0], filePath, jsonFile)
        else:
            setDefault(file[0][0], "", jsonFile)
    return

updateJsonExcel()

# def userUpdateJson(key, value):
#     setDefault(key, value, jsonFile)
#     return

def loadJson(self):
    with open(self.jsonPath, "r") as f:
        # userDefault is the entire json
        # jsonValue is the key
        userDefaults = json.load(f)
    return userDefaults

def defaultCheck(jsonValue, userDefaults):

    if jsonValue == "Customize Date":
        path = userDefaults.get(jsonValue)
        if path == "true":
            return {"location": "defaultCheck, key found, path valid", 
                    "error": "None",
                    "value": path,
                    "bool": True}
        else:
            return {"location": "defaultCheck, key found, path not valid",
                    "error": "create key, value pair",
                    "value": path,
                    "bool": False}

    # check if the value is inside
    if jsonValue in userDefaults or userDefaults[jsonValue]:
        # best way to get a json value
        path = userDefaults.get(jsonValue)

        # print( "\n" + jsonValue + "\n")
        # print("\n" + path + "\n")
        # print(jsonValue)
        # print(userDefaults)

        # tests to see if path returns None and a number
        if not path or not isinstance(path, str): # if path returns None, it is True, because None is falsy
            return {"location": "defaultCheck, path blank",
                    "error":"create key, value pair",
                    "value": path,
                    "bool": False}
        # return f"{jsonValue} found"
        # return path
        elif (os.path.exists(path) == True):
            # return True
            return {"location": "defaultCheck, key found, path valid", 
                    "error": "None",
                    "value": path,
                    "bool": True}
        else:
            # return False
            return {"location": "defaultCheck, key found, path not valid",
                    "error": "create key, value pair",
                    "value": path,
                    "bool": False}
    else:
        # return False
        return {"location": "defaultCheck, key not seen",
                "error":"create key, value pair",
                "value": path,
                "bool": False}

class Api:
    def __init__(self, window, jsonPath=jsonFile):
        self.jsonPath = jsonPath
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
        self.window = window

 # this is intialized on js. js sends model and whisper test immediately on startup
    def loadUserDefaults(self, jsonValue):
        try:
            if os.path.exists(self.jsonPath):
                # if there is a json file load it
                userDefaults = loadJson(self)

                # check value sent from json to see if it is present
                print(userDefaults)
                requestedValue = defaultCheck(jsonValue, userDefaults)
                # print(requestedValue["bool"])
                # return findings
                return requestedValue

            # if there is no json file, make one
            else:
                userDefaults = createJson()
                requestedValue = False
                # need to send a request to select model
                return requestedValue
            
        except Exception as e:
            print(e)
            return {"location": "exception block",
                    "value": "create key, value pair"}

    def checkUserDefaults(self, jsonValue):
        try:
            print(jsonValue)
            if os.path.exists(self.jsonPath):
                # if there is a json file load it
                userDefaults = loadJson(self)

                # check value sent from json to see if it is present
                print(userDefaults)
                requestedValue = defaultCheck(jsonValue, userDefaults)
                return requestedValue
                # return requestedValue["bool"]                
            else:
                createJson()
                requestedValue = defaultCheck(jsonValue, userDefaults)
                return requestedValue
            
        except Exception as e:
            print(e)
            return requestedValue

    def selectCustomDateFile():
        result = messagebox.askyesno(
            "Confirmation",
            "Would you like to customize the dates?"
        )
        print(f"User selected: {result}")  # True or False

        setDefault("Customize Date", result, jsonFile)

        
        return result

    def selectBalanceFile(self):
        self.balanceFilePath = filedialog.askopenfilename(
            title="Select a Balance file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.balanceFilePath)

        setDefault("Balance", self.balanceFilePath, jsonFile)

        return self.balanceFilePath
    
    def selectScheduleFile(self):
        self.scheduleFilePath = filedialog.askopenfilename(
            title="Select a Schedule file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.scheduleFilePath)

        setDefault("Schedules", self.scheduleFilePath, jsonFile)

        return self.scheduleFilePath
    
    def selectSalesFile(self):
        self.salesFilePath = filedialog.askopenfilename(
            title="Select a Sales file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.salesFilePath)

        setDefault("Sales", self.salesFilePath, jsonFile)

        return self.salesFilePath
    
    def customizeDate(self, bool):
        self.customizeDateBool = bool
        print(bool, type(bool))

        setDefault("Customize Date", self.customizeDateBool, jsonFile)

        return self.customizeDateBool
    
    def selectInvoiceFile(self):
        self.invoiceFilePath = filedialog.askopenfilename(
            title="Select a Invoice file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.invoiceFilePath)

        setDefault("Invoices", self.invoiceFilePath, jsonFile)

        return self.invoiceFilePath
    
    def selectHotelFile(self):
        self.hotelFilePath = filedialog.askopenfilename(
            title="Select a Hotel file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        )
        print(self.hotelFilePath)

        setDefault("Hotel - Schedule", self.hotelFilePath, jsonFile)

        return self.hotelFilePath

    def selectDestinationFolder(self):
        self.destinationFolderPath = filedialog.askdirectory(
            title="Select a Folder For New Yearly Directory"
        )
        print(self.destinationFolderPath)
        
        setDefault("Destination Folder", self.destinationFolderPath, jsonFile)
        
        return self.destinationFolderPath
    
    def dateSelection(self, dateInput):
        self.yearValue = int(dateInput)

        print(self.yearValue)

        setDefault("Year", self.yearValue, jsonFile)

        return self.yearValue
    
    def initializeBuildDirectory(self):
        def startThreading():
            
            self.sourceDir, self.files, self.nameExcel, self.nameSolo, self.nameNumberedExcel = initTemplate(self, templateFolderDir)

            DestDir = self.destinationFolderPath
            SourceDir = self.sourceDir
            FileName = self.nameSolo
            Files = self.nameNumberedExcel
            year = self.yearValue
            response = self.customizeDateBool

            
            print(self.window)
            self.window = webview.active_window()
            print(self.window)

            # current = webview.active_window()
            # print(current)

            automation(DestDir, SourceDir, FileName, Files, year, response, self)
            
            status(year, 100, "Completed", self)

        threading.Thread(target=startThreading, daemon=True).start()
        
        # Use daemon=True for background work like progress updates, file automation, etc., where it’s OK to stop when the app closes.
        # Use daemon=False if the task must complete before the program exits (e.g., saving files, database writes, etc.).

        return
        
# change date input to year
# setup json
# make invoice shortcut to each invoice folder
     

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
    # main()
    api = Api(None)

    # Open the HTML file in a webview window
    window = webview.create_window("Directory Builder", f"file://{html_file}", js_api=api)
    
    # Set the api self.window so python can push to it
    webview.start()
    # webview.start(debug=True)