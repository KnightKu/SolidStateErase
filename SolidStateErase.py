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


#First we delete the Path. 
shutil.rmtree(myPath)

# Then we regenerate the path. 
if not os.path.exists(myPath):
    os.makedirs(myPath)

# We Copy the seed text over 
shutil.copy2('lorem.txt', (myPath))

# We change our working Directory to myPath
os.chdir(myPath)

# Then we obtain how much free space is on the drive and print as well as save to a varible.

statvfs = os.statvfs(myPath)

freeBytes = statvfs.f_frsize * statvfs.f_bfree
print " It looks like you have %r Free bytes on this drive, I will Attempt to seed sudo-random text over it" %(freeBytes)
 

               #############################
# #######Filling up the drive with random seed data########

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
size = freeBytes # This should be equal to the drive space free. 
fname = "text.txt"
fh = open(fname, 'w')
while os.path.getsize(fname) < size:
    fh.write(g.next())

shutil.rmtree(myPath)


