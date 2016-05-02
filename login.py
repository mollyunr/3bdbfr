import sys
import datetime
import time
#
# Takes [database username password] as arguments
#

def attemptLogin(database, attempted_user, password):
    action = 'login_attempt'
    found = 'false'
    privileges = 'none'
    t = time.time()
    timestamp = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

    try:
        f = open("databases/" + database + '/' + attempted_user + "/userInfo.txt", 'r')
    except IOError:
        return "Not Found."

    temp = list(f)
    f.close()
    for index in range(0, len(temp)):
        temp[index] = temp[index].strip('\n');

    if password == temp[1]:
        found = "true"
        privileges = temp[2]
        
    else:
        return "Password is incorrect."

    f = open('log.txt', 'a')
    f.write(timestamp + '\n')
    f.write(action + '\n')
    f.write('attempted user: ' + attempted_user + '\n')
    f.write('user found: ' + found + '\n')
    f.write('user privileges: ' + privileges + '\n' + '\n')
    f.close()
    
    return privileges

if __name__ == '__main__':
    attemptLogin(sys.argv[1],sys.argv[2],sys.argv[3])
