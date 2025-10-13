import json

# update user to the progress of the setup
# import this function to createDirectory

def status(current, total, item, self):
    print("status function called")
    print(current)
    print(total)
    print(item)
    print(self)
    print(self.window)

    if item == "Completed":
        # data = {
        #     "progressValue": 100,
        #     "progressDescription": f"✅ {current} Directory Built"
        # }

        # json_data = json.dumps(data)

        # self.window.evaluate_js(f"handleProgress({json_data})")

        self.window.evaluate_js(f"updateProgress(100)")
        self.window.evaluate_js(f"progressStatusUpdate('✅ {current} Directory Built')")
        return

    progress = round((int(current)/total)*100)
    print(f"⏳ {progress}% of {item}")

    # SEND AS JSON
    # data = {
    #     "progressValue": progress,
    #     "progressDescription": f"⏳ {progress}% of {item}"
    # }
    
    # json_data = json.dumps(data)

    # self.window.evaluate_js(f"handleProgress({json_data})")

    self.window.evaluate_js(f"updateProgress({progress})")
    self.window.evaluate_js(f"progressStatusUpdate('{progress}% of {item}')")

    # can pass values from Python to JS using string interpolation or JSON.