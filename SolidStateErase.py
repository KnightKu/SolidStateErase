import subprocess,getpass
import os, sys
import errno
import functools
import Tkinter, tkFileDialog
root = Tkinter.Tk()
#Starting path of the file explorer for Tkinter
myPath = tkFileDialog.askdirectory(parent=root, initialdir="/",
title='Directory to destroy')

password = getpass.getpass()
#proc = subprocess.Popen(
#  ['sudo','rm','','-rf',(path)],
#   stdin=subprocess.PIPE)
proc = subprocess.Popen(
    ['sudo','rm','','-rf',(myPath+"/")],
    stdin=subprocess.PIPE)
proc.stdin.write(password+'\n')
proc.stdin.close()
proc.wait()
######################################################
# This is the begining of the Sudo Random Text Generator#


# First we get free Bytes Availible

statvfs = os.statvfs(myPath)

freeBytes = statvfs.f_frsize * statvfs.f_bfree

print freeBytes

##Then  we Hand off (freeBytes) to sudo-rand text process.



seed = "1092384956781341341234656953214543219"
words = open("lorem.txt", "r").read().replace("\n", '').split()
fdata(myPath)
fdata():
    a = collections.deque(words)
    b = collections.deque(seed)
    while True:
        yield ' '.join(list(a)[0:1024])
        a.rotate(int(b[0]))
        b.rotate(1)

g = fdata()
size = freeBytes # This should be equal to the drive space free. 
fname = "Omnomnom.nom"
fh = open(fname, 'w')
while os.path.getsize(fname) < size:
    fh.write(g.next())
## Then we need to call the wiping Utility once again. 

