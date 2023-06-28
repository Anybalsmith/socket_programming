import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("socket creation failed with error %s" %(err))
    sys.exit()
print("Socket successfully created")

target_host = input ("Enter the host name to connect: ")
target_port = int(input("Enter the port number to connect: "))
try:
    s.connect((target_host, target_port))
    print("Socket successfully connected to %s on port %s" %(target_host, target_port))
    s.shutdown(2)
except socket.error as err:
    print("Connection to %s on port %s failed with error %s" %(target_host, target_port, err))
    sys.exit()
