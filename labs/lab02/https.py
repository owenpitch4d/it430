#!/usr/bin/python3
# https.py
from socket import *

sock = socket(AF_INET, SOCK_STREAM) #ipv4 and tcp
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1) #socket options
sock.bind(("0.0.0.0", 8000))
sock.listen()

while True:
    client_sock, client_addr = sock.accept()
    print("connection from", client_addr)

    data = client_sock.recv(1024).decode() #binary to string
    lines = data.splitlines()
    uri = lines[0].split()[1].strip('/') # get uri to open

    try:
        if uri == '': uri = 'index.html' #automatically direct to index page
        f = open(uri, "rb") #open as bytes
        
    except FileNotFoundError:
        response_line = b"HTTP/1.1 404 NOT FOUND\r\n"
        client_sock.send(response_line)
        client_sock.close()
        break

    response_line = b"HTTP/1.1 200 OK\r\n" #response line
    response_body = f.read()
    
    headers = "".join([
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(response_body)}\r\n\r\n"
    ])

    response = response_line + headers.encode() + response_body

    client_sock.send(response)
    client_sock.close()

sock.close()