import os
from Tkinter import *

class LoginWindow(Frame):
    def login(self):
        username = self.loginWidget_username.get()
        password = self.loginWidget_password.get()
        if username and password:
            os.system('python login.py ' + username + ' ' + password)
        self.master.destroy()

    def createWidgets(self):
        self.usernameLabel = Label(self, text = 'Username: ').grid(row = 0, column = 0)
        loginStringValue_username = StringVar()
        self.loginWidget_username = Entry(self, textvariable = loginStringValue_username)
        self.loginWidget_username.grid(row = 0, column = 1)

        self.passwordLabel = Label(self, text = 'Password: ').grid(row = 1, column = 0)
        loginStringValue_password = StringVar()
        self.loginWidget_password = Entry(self, textvariable = loginStringValue_password)
        self.loginWidget_password.grid(row = 1, column = 1)

        self.LOGIN = Button(self)
        self.LOGIN['text'] = 'Login'
        self.LOGIN['command'] = self.login
        self.LOGIN.grid(row = 2, column = 1)

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
