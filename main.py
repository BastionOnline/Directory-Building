import webview
import sys
import threading
import traceback
import json
import os
from datetime import datetime
from modules.apiModule import Api, loadJson
from modules.TKInter.pyinstallerBoilerplate import pyinstallerboilerplate
from modules.initTemplateModule import initTemplate
from modules.automationModule import automation
from modules.statusModule import status


# change date input to year
# make invoice shortcut to each invoice folder
html_file, css_file, js_file = pyinstallerboilerplate()

if __name__ == '__main__':
    # used by task scheduler to start with arg
    if len(sys.argv) > 1:
    # start using next year
        if os.path.exists("./templates"):
            # def startThreading():
                try:
                    # with open("./templates", "r") as f:
                    #     # userDefault is the entire json
                    #     # jsonValue is the key
                    #     heist = json.load(f)

                    # heist = loadJson(self)

                    DestDir = r"C:\Users\Coat Check\OneDrive\MTCC"
                    # year = int(heist["Year"])
                    autoDay = datetime.today()
                    print(autoDay)
                    year = autoDay.year + 1
                    print(year)
                    response = "true"
                    SourceDir = os.path.join(os.getcwd(), "templates")
                    FileName = ['Balance', 'Schedules', 'Sales', 'Invoices', 'Hotel - Schedule']
                    Files = ['1. Balance.xlsm', '2. Schedules.xlsx', '3. Sales.xlsx', '4. Invoices.xlsx', '5. Hotel - Schedule.xlsx']
                    
                    automation(DestDir, SourceDir, FileName, Files, year, response)
                    # status(year, 100, "Completed", self)


                except Exception as e:
                    with open("error_log.txt", "w") as f:
                        f.write(traceback.format_exc())
            # threading.Thread(target=startThreading, daemon=True).start()



    else:
        # main()
        api = Api(None)

        # Open the HTML file in a webview window
        window = webview.create_window("Directory Builder", f"file://{html_file}", js_api=api)
        
        # Set the api self.window so python can push to it
        webview.start()
        # webview.start(debug=True)