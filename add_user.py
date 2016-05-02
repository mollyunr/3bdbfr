import sys
import datetime
import time
import os

#
# Takes [username password privileges database_name] as arguments
#


def add(username, password, privileges, database_name):
    action = 'add_user'
    created = 'false'
    t = time.time()
    timestamp = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

    f = open('userdatabase.txt', 'r')
    fileLength = sum(1 for line in f)
    f.close()

    f = open('userdatabase.txt', 'r')
    temp = list(f)
    f.close()

    for index in range(0, fileLength):
        temp[index] = temp[index].split();

    if not os.path.exists("databases/" + database_name + '/' + username):
        os.mkdir("databases/" + database_name + '/' + username)
        created = True

        new_user = []
        new_user.append(username)
        new_user.append(password)
        new_user.append(privileges)

        temp.append(new_user)

        f = open('userdatabase.txt', 'w')
        for index in range(0, len(temp)):
            f.write(temp[index][0] + ' ' + temp[index][1] + ' ' + temp[index][2] + '\n')
        f.close()

        f = open('log.txt', 'a')
        f.write(timestamp + '\n')
        f.write(action + '\n')
        f.write('user: ' +username + '\n')
        f.write('privileges: ' + privileges + '\n')
        f.write('database name: ' + database_name + '\n' + '\n')
        f.close()

    return created
