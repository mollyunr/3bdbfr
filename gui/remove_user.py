import os
from Tkinter import *

class RemoveUser(Frame):
    def remove_user(self):
        username = self.removeUserWidget_username.get()
        databaseName = self.removeUserWidget_databaseName.get()
        os.system('python remove_user.py ' + username + ' ' + databaseName)

    def createWidgets(self):
        # remove user string handling and fields/button
        self.usernameLabel = Label(self, text = "User name: ").grid(row = 0, column = 0)
        removeUserStringValue_username = StringVar()
        self.removeUserWidget_username = Entry(self, textvariable = removeUserStringValue_username)
        self.removeUserWidget_username.grid(row = 0, column = 1)

        self.databaseLabel = Label(self, text = "Database: ").grid(row = 1, column = 0)
        removeUserStringValue_databaseName = StringVar()
        self.removeUserWidget_databaseName = Entry(self, textvariable = removeUserStringValue_databaseName)
        self.removeUserWidget_databaseName.grid(row = 1, column = 1)

        self.REMOVE_USER = Button(self)
        self.REMOVE_USER['text'] = 'Remove User'
        self.REMOVE_USER['command'] = self.remove_user
        self.REMOVE_USER.grid(row = 2, column = 1)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()