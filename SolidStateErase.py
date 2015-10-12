import subprocess,getpass
import os, sys
import errno
import functools
import Tkinter, tkFileDialog
root = Tkinter.Tk()
import collections
import shutil
#Starting path of the file explorer for Tkinter
myPath = tkFileDialog.askdirectory(parent=root, initialdir="/",
title='Directory to destroy')

# a new way we can Destroy A directory ;)
shutil.rmtree(myPath)
if not os.path.exists(myPath):
    os.makedirs(myPath)

# hold as well password = getpass.getpass()
#proc = subprocess.Popen(
#  ['sudo','rm','','-rf',(path)],
#   stdin=subprocess.PIPE)
""" # This is on hold Until we can figure out the bug.
proc = subprocess.Popen(
    ['sudo','rm','',(myPath+"/")],
    stdin=subprocess.PIPE)
proc.stdin.write(password+'\n')
proc.stdin.close()
proc.wait()
if proc.returncode == 0:
    pass 
"""
# put code that must only run if successful here.
######################################################
# This is the begining of the Sudo Random Text Generator#


# First we get free Bytes Availible

statvfs = os.statvfs(myPath)

freeBytes = statvfs.f_frsize * statvfs.f_bfree

print freeBytes

##Then  we Hand off (freeBytes) to sudo-rand text process.

#This was a method found online that attaches a Lorem Ipsum text to quickly generate data files. 

#needs lorem.txt in .py dir. 

seed = "1092384956781341341234656953214543219"
words = open("lorem.txt", "r").read().replace("\n", '').split()

def fdata():
    a = collections.deque(words)
    b = collections.deque(seed)
    while True:
        yield ' '.join(list(a)[0:1024])
        a.rotate(int(b[0]))
        b.rotate(1)

g = fdata()
size = 10235 # This should be equal to the drive space free. 
fname = "text.txt"
fh = open(fname, 'w')
while os.path.getsize(fname) < size:
    fh.write(g.next())

fdata()
## Then we need to call the wiping Utility once again. 

