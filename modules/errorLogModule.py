import traceback
from datetime import datetime

def errorLog(e):
    timestamp = datetime.now().strftime("%a, %b %d, %Y, %I:%M %p")
    with open("error_log.txt", "a") as log:
        log.write(f"\n[{timestamp}] ERROR: {type(e).__name__}: {e}\n{traceback.format_exc()}\n{'-'*60}\n")
