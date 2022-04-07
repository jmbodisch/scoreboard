import string

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

def sort_config(config):
    sortedFiles = sorted(config["files"], key=lambda file: file["order"])
    config["files"] = sortedFiles

def update_order(config, oldIndex, newIndex):
    sortedFiles = sorted(config["files"], key=lambda file: file["order"])
    sortedFiles[oldIndex]["order"] = newIndex
    sortedFiles[newIndex]["order"] = oldIndex
    sortedFiles = sorted(config["files"], key=lambda file: file["order"])
    config["files"] = sortedFiles