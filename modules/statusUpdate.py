# update user to the progress of the setup
# import this function to createDirectory

def status(current, total, item, self):
    print("status function called")
    print(current)
    print(total)
    print(item)
    print(self)
    print(self.window)


    progress = round((int(current)/total)*100)
    print(f"{progress}% of {item}")

    # self.window.evaluate_js('alert("Hello from Python!")')
    # self.window.evaluate_js('ring()')
    # self.window.evaluate_js('alertTest()')
    # self.window.evaluate_js(f"updateProgress()")
    self.window.evaluate_js(f"updateProgress({progress})")
    self.window.evaluate_js(f"progressStatusUpdate('{progress}% of {item}')")

    # can pass values from Python to JS using string interpolation or JSON.
    