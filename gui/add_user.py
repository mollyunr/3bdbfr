#!/usr/bin/python
import os
from Tkinter import *

class AddUserWindow(Frame):
    def add_user(self):
        username = self.addUserWidget_username.get()
        password = self.addUserWidget_password.get()
        privileges = self.addUserWidget_privileges.get()
        databaseName = self.addUserWidget_databaseName.get()
        os.system('python add_user.py ' + username + ' ' + password + ' ' + privileges + ' ' + databaseName)

    def createWidgets(self):
        # add user string handling and fields/button
        self.usernameLabel = Label(self, text = "Username: ").grid(row = 0, column = 0)
        addUserStringValue_username = StringVar()
        self.addUserWidget_username = Entry(self, textvariable = addUserStringValue_username)
        self.addUserWidget_username.grid(row = 0, column = 1)

        self.passwordLabel = Label(self, text = "Password: ").grid(row = 1, column = 0)
        addUserStringValue_password = StringVar()
        self.addUserWidget_password = Entry(self, textvariable = addUserStringValue_password)
        self.addUserWidget_password.grid(row = 1, column = 1)

        self.privilegesLabel = Label(self, text = "Privileges: ").grid(row = 2, column = 0)
        addUserStringValue_privileges = StringVar()
        self.addUserWidget_privileges = Entry(self, textvariable = addUserStringValue_privileges)
        self.addUserWidget_privileges.grid(row = 2, column = 1)

        self.databaseLabel = Label(self, text = "Database: ").grid(row = 3, column = 0)
        addUserStringValue_databaseName = StringVar()
        self.addUserWidget_databaseName = Entry(self, textvariable = addUserStringValue_databaseName)
        self.addUserWidget_databaseName.grid(row = 3, column = 1)

        self.ADD_USER = Button(self)
        self.ADD_USER['text'] = 'Add User'
        self.ADD_USER['command'] = self.add_user
        self.ADD_USER.grid(row = 4, column = 1)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
