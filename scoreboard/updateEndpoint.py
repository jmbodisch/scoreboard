
def updateFile(file, newValue):

    if(validateInput(file, newValue)):
        writeFile(file, newValue)
    else:
        return "failed"
    return newValue

def getValue(file):
    file = open(file["path"], "r")
    response = file.read()
    file.close()
    return response

def validateInput(file, newValue):
    return True

def writeFile(file, newValue):
    editable = open(file["path"], "r+")
    editable.write(newValue)
    editable.truncate()
    editable.close()