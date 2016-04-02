import sys
import datetime
import time
import os

#
# Takes database name as argument
#

arguments = len(sys.argv)

action = 'create_database'
log = 'false'
t = time.time()
timestamp = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

f = open('userdatabase.txt', 'r')
fileLength = sum(1 for line in f)
f.close()

if fileLength > 0 and arguments > 1:
    f = open('userdatabase.txt', 'r')
    temp = list(f)
    f.close()

    for index in range(0, fileLength):
        temp[index] = temp[index].split();

    if not os.path.exists(sys.argv[1]):
        os.mkdir(sys.argv[1])
        log = 'true'

    for index in range(0, fileLength):
        if not os.path.exists(sys.argv[1] + '/' + temp[index][0]):
            os.mkdir(sys.argv[1] + '/' + temp[index][0])

    path, dirs, files = os.walk(sys.argv[1]).next()
    directory_count = len(dirs)
    database_size = os.path.getsize(sys.argv[1])

    path, dirs, files = os.walk(sys.argv[1] + '/' + temp[0][0]).next()
    picture_count = len(files)

    f = open(sys.argv[1] + '/' + 'database_information.txt', 'w')
    f.write('users: ' + str(directory_count) + '\n')
    f.write('database size: ' + str(database_size) + ' bytes' + '\n')
    f.write('pictures per user: ' + str(picture_count) + '\n')
    f.close()

    if log == 'true':
        f = open('log.txt', 'a')
        f.write('\n' + timestamp + '\n')
        f.write(action + '\n' + '\n')
        f.close()


f = open('context.txt', 'w')

if log == 'true':
    f.write('database created\n')
else:
    f.write('database of the same name already exists\n')

f.close()
