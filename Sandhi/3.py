from subprocess import *
from os import *
from time import *

def mv_files(files):
    """
    This function accept a list of file names in the download folder
    and check for files with extension .txt,.jpg,.mpg
    and moves these files to proper folders such as 
    Pictures,Documents,Videos
    """
    for fil in files:
	# splits the file name and checks the extensions
	ext = fil.split('.')[-1]
        if ext == 'txt' or ext == 'pdf':
            call(["mv",downloads+fil,home+"Documents"])
    	elif ext == 'jpg' or ext == 'png':
            call(["mv",downloads+fil,home+"Pictures"])
	elif ext == 'mpg' or ext == 'mp4' or ext == 'flv':
           call(["mv",downloads+fil,home+"Videos"])
	elif ext == 'mp3':
	    call(["mv",downloads+fil,home+"Music"])

def read_files():
    files = check_output(["ls",downloads])
    files = files.split("\n")
    return files

if __name__ == "__main__":
    home = path.expanduser('~')+"/"
    downloads = home+"Downloads/"
    while True:
	    mv_files(read_files())
	    sleep(.01)
