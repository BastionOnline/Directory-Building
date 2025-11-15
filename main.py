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
        # print(len(sys.argv))
        # print(sys.argv[1])
        # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # sourceDir = os.path.join(BASE_DIR, "templates")
        sourceDir = r"C:\Users\Coat Check\OneDrive\MTCC\0. Admin Operations - Computer Templates\Yearly Directory Builder\templates"
        # # sourceDir = os.path.join(os.getcwd(), "templates")
        # print(f"BaseDir: {BASE_DIR}")
        # print(f"sourceDir: {sourceDir}")
        # input("type something")

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
                print(e)
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