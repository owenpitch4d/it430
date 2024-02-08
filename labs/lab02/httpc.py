#!/usr/bin/python3
# httpc.py

from socket import *
from sys import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((argv[1], 80))
request_line = b"GET / HTTP/1.1\r\n"
host = f"Host: {argv[1]}\r\n"
lang = b"Accepted-Language: en\r\n\r\n"

sock.send(request_line + host.encode() + lang)
data = sock.recv(1024)
print(data.decode())