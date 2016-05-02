import sys
import datetime
import time
import os

#
# Takes [username password privileges database_name] as arguments
#

def findUser(username, database_name):
    if os.path.exists("databases/" + database_name + '/' + username):
        return True
    else:
        return False

def add(username, password, privileges, database_name):
    action = 'add_user'
    created = False
    t = time.time()
    timestamp = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

    if not findUser(username, database_name):
        os.mkdir("databases/" + database_name + '/' + username)
        f = open("databases/" + database_name + '/' + username + '/' + "userInfo.txt", 'w')
        f.write(username + '\n' + password + '\n' + privileges)
        f.close()

        created = True

        f = open('log.txt', 'a')
        f.write(timestamp + '\n')
        f.write(action + '\n')
        f.write('user: ' + username + '\n')
        f.write('privileges: ' + privileges + '\n')
        f.write('database name: ' + database_name + '\n' + '\n')
        f.close()

    return created

if __name__ == '__main__':
    add(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
