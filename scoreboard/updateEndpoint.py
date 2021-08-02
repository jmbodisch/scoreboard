
def updateFile(file, newValue):

    if(validateInput(file, newValue)):
        writeFile(file, newValue)
        return
    else:
        print("invalid input")
        return
    return

def validateInput(file, newValue):
    return True

def writeFile(file, newValue):
    editable = open(file["path"], "r+")
    editable.write(newValue)
    editable.truncate()
    editable.close()