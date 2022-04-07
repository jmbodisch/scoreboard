import string

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

def sort_config(config):
    sortedFiles = sorted(config["files"], key=lambda file: file["order"])
    for file in sortedFiles:
        print(file["name"] + str(file["order"]))
    config["files"] = sortedFiles