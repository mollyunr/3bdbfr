import sys
import datetime
import time
import os

#
# Takes database name as argument
#

def create(databaseName):

    action = 'create_database'
    log = 'false'
    t = time.time()
    timestamp = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
    path = "databases/" + databaseName

    if not os.path.exists(path):
        os.mkdir(path)
        log = 'true'

    if log == 'true':
        f = open('log.txt', 'a')
        f.write('\n' + timestamp + '\n')
        f.write(action + '\n' + '\n')
        f.close()
        return True

    else:
        return False
