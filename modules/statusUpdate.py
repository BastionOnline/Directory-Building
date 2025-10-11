# update user to the progress of the setup
# import this function to createDirectory

def status(current, total, item, self):
    progress = round((int(current)/total)*100)
    print(f"{progress}% of {item}")
    