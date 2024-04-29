'''Methods to assist the application with modifying files.'''
from os.path import exists

def update_file(root, file, new_value):
    '''
    Wrapper to validate input before updating the contents of the file on the host system.
    '''

    if validate_input():
        write_file(root, file, new_value)
    else:
        return 'failed'
    return new_value

def get_value(root, file):
    '''
    Gets the contents of a text file on the host system.
    '''
    if exists(root+file['path']):
        with open(root+file['path'], 'r', encoding='utf-8') as outfile:
            response = outfile.read()
            outfile.close()
    else:
        response = ''
    return response

def validate_input():
    '''
    TODO: Implement input validation based on the type of file being modified.
    '''
    return True

def write_file(root, file, new_value):
    '''
    Writes to a file on the host system.
    '''
    new_value = new_value.replace('\r', '')
    if exists(root+file['path']):
        editable = open(root+file['path'], 'r+', encoding='utf-8')
    else:
        editable = open(root+file['path'], 'w+', encoding='utf-8')
    editable.write(new_value)
    file['value'] = new_value
    editable.truncate()
    editable.close()
