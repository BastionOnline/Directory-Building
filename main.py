import webview
import sys
import traceback
import os
from datetime import datetime
from modules.apiModule import Api
from modules.TKInter.pyinstallerBoilerplate import pyinstallerboilerplate
from modules.automation.automationModule import automation

# change date input to year
# make invoice shortcut to each invoice folder
html_file, css_file, js_file = pyinstallerboilerplate()

if __name__ == '__main__':
    # used by task scheduler to start with arg
    if len(sys.argv) > 1:

        sourceDir = os.path.join(os.getcwd(), "templates")

        if os.path.exists(sourceDir):
            try:
                destDir = r"C:\Users\Coat Check\OneDrive\MTCC"
                autoDay = datetime.today()
                print(autoDay)
                
                # start using next year
                year = autoDay.year + 1
                print(year)
                response = "true"

                FileName = ['Balance', 'Schedules', 'Sales', 'Invoices', 'Hotel - Schedule']
                Files = ['1. Balance.xlsm', '2. Schedules.xlsx', '3. Sales.xlsx', '4. Invoices.xlsx', '5. Hotel - Schedule.xlsx']
                
                automation(destDir, sourceDir, FileName, Files, year, response)

            except Exception as e:
                timestamp = datetime.now().strftime("%a, %b %d, %Y, %I:%M %p")
                with open("error_log.txt", "a") as log:
                    log.write(f"\n[{timestamp}]\n{traceback.format_exc()}\n{'-'*60}\n")

    else:
        # main()
        api = Api(None)

        # Open the HTML file in a webview window
        window = webview.create_window("Directory Builder", f"file://{html_file}", js_api=api)
        
        # Set the api self.window so python can push to it
        webview.start()
        # webview.start(debug=True)