import sys
import datetime
import time
import os
import shutil
import add_user

#
# Takes [username database_name] as arguments
#
def remove(user, database_name):
    action = 'remove_user'
    removed = False
    t = time.time()
    timestamp = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

    if add_user.findUser(user, database_name):
        shutil.rmtree("databases/" + database_name + '/' + user)

        removed = True

        f = open('log.txt', 'a')
        f.write(timestamp + '\n')
        f.write(action + '\n')
        f.write('user: ' + user + '\n')
        f.write('database name: ' + database_name + '\n' + '\n')
        f.close()

    return removed

if __name__ == '__main__':
    remove(sys.argv[1])
