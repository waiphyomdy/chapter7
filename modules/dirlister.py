import os

def run(**args):
    print  "[*]In dirlister moudle."
    files = os.listdir(".")
    return str(files)
