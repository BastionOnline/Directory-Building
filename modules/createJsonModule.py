import os
from datetime import datetime
import json


def createJson(templateFolderStat, templateFolderDir, jsonFile):
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