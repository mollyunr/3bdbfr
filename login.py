import sys
import datetime
import time

#
# Takes [username password] as arguments
#

arguments = len(sys.argv)

action = 'login_attempt'
attempted_user = sys.argv[1]
found = 'false'
privileges = 'none'
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

    for index in range(0, len(temp)):
        if sys.argv[1] == temp[index][0]:
            if sys.argv[2] == temp[index][1]:
                found = 'true'
                privileges = temp[index][2]

f = open('log.txt', 'a')
f.write(timestamp + '\n')
f.write(action + '\n')
f.write('attempted user: ' + attempted_user + '\n')
f.write('user found: ' + found + '\n')
f.write('user privileges: ' + privileges + '\n' + '\n')
f.close()

f = open('context.txt', 'w')
f.write(found + '\n')
f.write(privileges + '\n')
f.close()
