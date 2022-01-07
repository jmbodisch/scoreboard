
def updateFile(root, file, newValue):

    if(validateInput(file, newValue)):
        writeFile(root, file, newValue)
    else:
        return "failed"
    return newValue

def getValue(root, file):
    file = open(root+file["path"], "r")
    response = file.read()
    file.close()
    return response

def validateInput(file, newValue):
    return True

def writeFile(root, file, newValue):
    newValue = newValue.replace("\r", "")
    editable = open(root+file["path"], "r+")
    editable.write(newValue)
    file["value"] = newValue
    editable.truncate()
    editable.close()