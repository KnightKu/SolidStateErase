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

