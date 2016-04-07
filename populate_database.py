import sys
import shutil
import os

#
# Takes database name as argument
# 

arguments = len(sys.argv)

f = open('userdatabase.txt', 'r')
fileLength = sum(1 for line in f)
f.close()

if fileLength > 0 and arguments > 1:
    f = open('userdatabase.txt', 'r')
    temp = list(f)
    f.close()

    for index in range(0, fileLength):
        temp[index] = temp[index].split();

    for index in range(0, len(temp)):
        for indexTwo in range(0, 5):
            src = 'att_faces/s' + str(1 + index) + '/' + str(1 + indexTwo) + '.pgm'
            dest = sys.argv[1] + '/' + temp[index][0]
            shutil.copy2(src, dest)

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
