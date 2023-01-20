'''Assorted utility functions for scoreboard application.'''
import string

def format_filename(in_string):
    '''
    Formats a filename not to have spaces or invalid characters.
    '''
    valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
    filename = ''.join(c for c in in_string if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

def sort_config(config):
    '''
    Updates the scoreboard application's config object to be in sorted order.
    '''
    sorted_files = sorted(config["files"], key=lambda file: file["order"])
    config["files"] = sorted_files

def update_order(config, old_index, new_index):
    '''
    Updates the order of config items, and then updates the scoreboard application's config object.
    '''
    sorted_files = sorted(config["files"], key=lambda file: file["order"])
    sorted_files[old_index]["order"] = new_index
    sorted_files[new_index]["order"] = old_index
    sorted_files = sorted(config["files"], key=lambda file: file["order"])
    config["files"] = sorted_files
