import os
from Tkinter import *
from gui.login import LoginWindow

f = open('context.txt')
fileLength = sum(1 for line in f)
f.close()

f = open('context.txt')
text = list(f)
f.close()

for index in range(0, fileLength):
    text[index] = text[index].split()

if not text:
    text = ' '



count = 0

while text:
    print count
    count += 1

    root = Tk()
    root.resizable(width = False, height = False)
    root.geometry('{}x{}'.format(800,450))

    if text == ' ':
        window = LoginWindow(master = root)
        window.mainloop()
        # login

    elif text[0][0] == 'admin':
        print 'admin'
        # admin

    elif text[0][0] == 'user':
        print 'user'
        # user

    elif text[0][0] == 'quit':
        break

    f = open('context.txt')
    fileLength = sum(1 for line in f)
    f.close()

    f = open('context.txt')
    text = list(f)
    f.close()

    for index in range(0, fileLength):
        text[index] = text[index].split()

    if not text:
        text = ' '
