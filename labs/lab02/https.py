#!/usr/bin/python3
# https.py
from socket import *
import os

sock = socket(AF_INET, SOCK_STREAM) #ipv4 and tcp
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", 8500))
sock.listen()

while True:
    client_sock, client_addr = sock.accept()
    print("connection from", client_addr)

    data = client_sock.recv(1024).decode() #binary
    lines = data.splitlines()
    uri = lines[0].split()[1].strip('/')
    print(uri)

    try:
        if uri == '': uri = 'index.html'
        f = open(uri)
        response_body = f.read()
        f.close()
        
        response_line = "HTTP/1.1 200 OK\r\n\r\n"
    except FileNotFoundError:
        response_line = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
        response_body = "File Not Found"


    headers = "".join([
        "Content-Type: text/html\r\n"
    ])
    #response = "".join([response_line, headers, response_body])
    response = response_line + headers + response_body


    client_sock.sendall(response.encode())
    client_sock.close()

sock.close()