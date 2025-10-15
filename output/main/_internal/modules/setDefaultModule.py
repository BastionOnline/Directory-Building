import json

def setDefault(key, value, jsonPath):
# def setDefault(key, value, jsonPath=jsonFile):
    try:
        with open(jsonPath, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # Update the dictionary
    data[key] = value

    # Write the updated data back to the file (pretty format)
    with open(jsonPath, "w") as f:
        json.dump(data, f, indent=4)
    return
