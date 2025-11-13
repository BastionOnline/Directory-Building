from datetime import datetime
import json
import webview
import os
import threading
import traceback
import shutil
from tkinter import filedialog
from modules.initTemplateModule import initTemplate
from modules.automationModule import automation
from modules.statusModule import status

# load json file path
templateFolderDir = os.path.join(os.getcwd(), "templates")

jsonPath = "userDefaults.json"

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

    currentYear = datetime.now().year
    

    print(os.path.exists(jsonFile))
    if os.path.exists(jsonFile) == False:
        data = {
            "Year": f"{currentYear + 1}",
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


def loadJson(self):
    with open(self.jsonPath, "r") as f:
        # userDefault is the entire json
        # jsonValue is the key
        userDefaults = json.load(f)
    return userDefaults

def defaultCheck(jsonValue, userDefaults):
    print(jsonValue)
    print(userDefaults)

    if jsonValue == "Customize Date":
        path = userDefaults.get(jsonValue)
        print(path)
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
    elif jsonValue == "Year":
        path = userDefaults.get(jsonValue)

        # print(path, type(path))
        try:
            yearint = int(path)

            if type(yearint) == int:
                return {"location": "defaultCheck, key found, path valid", 
                        "error": "None",
                        "value": path,
                        "bool": True}
            else:
                return {"location": "defaultCheck, key found, path not valid",
                        "error": "create key, value pair",
                        "value": path,
                        "bool": False}
        except Exception as e:
            print(e)
            return {"location": "defaultCheck, exception block",
                    "error": "create key, value pair",
                    "value": path,
                    "bool": False}

    # check if the value is inside
    if jsonValue in userDefaults or userDefaults[jsonValue]:
        # best way to get a json value
        path = userDefaults.get(jsonValue)

        # tests to see if path returns None and a number
        if not path or not isinstance(path, str): # if path returns None, it is True, because None is falsy
            return {"location": "defaultCheck, path blank",
                    "error":"create key, value pair",
                    "value": path,
                    "bool": False}
        elif (os.path.exists(path) == True):
            return {"location": "defaultCheck, key found, path valid", 
                    "error": "None",
                    "value": path,
                    "bool": True}
        else:
            return {"location": "defaultCheck, key found, path not valid",
                    "error": "create key, value pair",
                    "value": path,
                    "bool": False}
    else:
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
            else:
                createJson()
                requestedValue = defaultCheck(jsonValue, userDefaults)
                return requestedValue
            
        except Exception as e:
            print(e)
            return requestedValue

    def selectBalanceFile(self):
        # use os.path.normpath to standardize path formats
        self.balanceFilePath = os.path.normpath(filedialog.askopenfilename(
            title="Select a Balance file",
            filetypes=[("Excel Files", "*.xls *.xlsx *.xlsm" )]
        ))
        print(self.balanceFilePath)

        filename = "1. Balance.xlsx"
        templateFolderFileCopy = os.path.join(templateFolderDir, filename)
        shutil.copyfile(self.balanceFilePath, templateFolderFileCopy)

        setDefault("Balance", self.balanceFilePath, jsonFile)

        return self.balanceFilePath
    
    def selectScheduleFile(self):
        self.scheduleFilePath = os.path.normpath(filedialog.askopenfilename(
            title="Select a Schedule file",
            filetypes=[("Excel Files", "*.xls *.xlsx *.xlsm" )]
        ))
        print(self.scheduleFilePath)

        filename = "2 Schedules.xlsx"
        templateFolderFileCopy = os.path.join(templateFolderDir, filename)
        shutil.copyfile(self.balanceFilePath, templateFolderFileCopy)

        setDefault("Schedules", self.scheduleFilePath, jsonFile)

        return self.scheduleFilePath
    
    def selectSalesFile(self):
        self.salesFilePath = os.path.normpath(filedialog.askopenfilename(
            title="Select a Sales file",
            filetypes=[("Excel Files", "*.xls *.xlsx *.xlsm" )]
        ))
        print(self.salesFilePath)

        filename = "3. Sales.xlsx"
        templateFolderFileCopy = os.path.join(templateFolderDir, filename)
        shutil.copyfile(self.balanceFilePath, templateFolderFileCopy)

        setDefault("Sales", self.salesFilePath, jsonFile)

        return self.salesFilePath
    
    def customizeDate(self, bool):
        self.customizeDateBool = bool
        print(bool, type(bool))

        setDefault("Customize Date", self.customizeDateBool, jsonFile)

        return self.customizeDateBool
    
    def selectInvoiceFile(self):
        self.invoiceFilePath = os.path.normpath(filedialog.askopenfilename(
            title="Select a Invoice file",
            filetypes=[("Excel Files", "*.xls *.xlsx *.xlsm" )]
        ))
        print(self.invoiceFilePath)

        filename = "4. Invoices.xlsx"
        templateFolderFileCopy = os.path.join(templateFolderDir, filename)
        shutil.copyfile(self.balanceFilePath, templateFolderFileCopy)

        setDefault("Invoices", self.invoiceFilePath, jsonFile)

        return self.invoiceFilePath
    
    def selectHotelFile(self):
        self.hotelFilePath = os.path.normpath(filedialog.askopenfilename(
            title="Select a Hotel file",
            filetypes=[("Excel Files", "*.xls *.xlsx *.xlsm" )]
        ))
        print(self.hotelFilePath)

        filename = "5. Hotel - Schedule.xlsx"
        templateFolderFileCopy = os.path.join(templateFolderDir, filename)
        shutil.copyfile(self.balanceFilePath, templateFolderFileCopy)

        setDefault("Hotel - Schedule", self.hotelFilePath, jsonFile)

        return self.hotelFilePath

    def selectDestinationFolder(self):
        self.destinationFolderPath = os.path.normpath(filedialog.askdirectory(
            title="Select a Folder For New Yearly Directory"
        ))
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
            try:

                print(self.window)
                self.window = webview.active_window()
                print(self.window)

                self.sourceDir, self.files, self.nameExcel, self.nameSolo, self.nameNumberedExcel = initTemplate(self, templateFolderDir)

                heist = loadJson(self)

                DestDir = heist["Destination Folder"]
                year = int(heist["Year"])
                response = heist["Customize Date"]
                SourceDir = self.sourceDir
                FileName = self.nameSolo
                Files = self.nameNumberedExcel
                
                automation(DestDir, SourceDir, FileName, Files, year, response, self)
                status(year, 100, "Completed", self)

            except Exception as e:
                with open("error_log.txt", "w") as f:
                    f.write(traceback.format_exc())

        threading.Thread(target=startThreading, daemon=True).start()
        
        # Use daemon=True for background work like progress updates, file automation, etc., where it’s OK to stop when the app closes.
        # Use daemon=False if the task must complete before the program exits (e.g., saving files, database writes, etc.).

        return
    
    def openBuildLocation(self):
        
        heist = loadJson(self)
        folder = heist["Destination Folder"]

        # Handle different OS
        # if platform.system() == "Windows":
        os.startfile(folder)
        return f"Opened: {folder}"
