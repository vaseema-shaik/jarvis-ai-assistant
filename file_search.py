import os

def search_file(filename, path="C:\\"):

    for root, dirs, files in os.walk(path):

        if filename in files:
            return os.path.join(root, filename)

    return "File not found"