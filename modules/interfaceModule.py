import webview
import os
import sys
from tkinter import filedialog

def interface():
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


    if __name__ == '__loadInterface__':
        # Example usage of transcribe function
        api = Api()

        # Open the HTML file in a webview window
        webview.create_window("Directory Builder", f"file://{html_file}", js_api=api)
        webview.start()

