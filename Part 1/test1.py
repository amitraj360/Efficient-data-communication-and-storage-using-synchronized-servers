import socket
import unittest

host="127.0.0.1"
port=5000
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send("check#alive")
data=s.recv(1024)
print(data)