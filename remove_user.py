import sys
import datetime
import time
import os

#
# Takes [username database_name] as arguments
#

arguments = len(sys.argv)

action = 'remove_user'
user = sys.argv[1]
database_name = sys.argv[2]
removed = 'false'
t = time.time()
timestamp = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

if arguments == 3:
    f = open('userdatabase.txt', 'r')
    fileLength = sum(1 for line in f)
    f.close()

    f = open('userdatabase.txt', 'r')
    temp = list(f)
    f.close()

    for index in range(0, fileLength):
        temp[index] = temp[index].split();

    if os.path.exists(database_name + '/' + user):
        print 'got here'
        os.rmdir(database_name + '/' + user)

        for index in range(0, fileLength):
            if temp[index][0] == user:
                del temp[index]

        f = open('userdatabase.txt', 'w')
        for index in range(0, len(temp)):
            f.write(temp[index][0] + ' ' + temp[index][1] + ' ' + temp[index][2] + '\n')
        f.close()

        path, dirs, files = os.walk(database_name).next()
        directory_count = len(dirs)
        database_size = os.path.getsize(database_name)

        path, dirs, files = os.walk(database_name + '/' + temp[0][0]).next()
        picture_count = len(files)

        f = open(database_name + '/' + 'database_information.txt', 'w')
        f.write('users: ' + str(directory_count) + '\n')
        f.write('database size: ' + str(database_size) + ' bytes' + '\n')
        f.write('pictures per user: ' + str(picture_count) + '\n')
        f.close()

        f = open('log.txt', 'a')
        f.write(timestamp + '\n')
        f.write(action + '\n')
        f.write('user: ' + user + '\n')
        f.write('database name: ' + database_name + '\n' + '\n')
        f.close()

f = open('context.txt', 'w')
if removed == 'true':
    f.write('user removed')
else:
    f.write('user does not exist')
f.close()
