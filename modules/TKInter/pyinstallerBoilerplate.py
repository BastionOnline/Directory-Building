import sys
import os

def pyinstallerboilerplate():

    def resource_path(relative_path):
        """ Get the absolute path to a resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temporary folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


    # enable for debugging
    html_file = resource_path(r'.\index.html')
    css_file = resource_path(r'.\assets\style.css')
    js_file = resource_path(r'.\assets\script.js')

    return html_file, css_file, js_file