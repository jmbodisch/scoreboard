from os.path import exists

def updateFile(root, file, newValue):

    if(validateInput(file, newValue)):
        writeFile(root, file, newValue)
    else:
        return "failed"
    return newValue

def getValue(root, file):
    if exists(root+file["path"]):
        file = open(root+file["path"], "r")
        response = file.read()
        file.close()
    else:
        response = ""
    return response

def validateInput(file, newValue):
    return True

def writeFile(root, file, newValue):
    newValue = newValue.replace("\r", "")
    if exists(root+file["path"]):
        editable = open(root+file["path"], "r+")
    else:
        editable = open(root+file["path"], "w+")
    editable.write(newValue)
    file["value"] = newValue
    editable.truncate()
    editable.close()