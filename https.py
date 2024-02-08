#!/usr/bin/python3
# https.py
from socket import *
import os

def parseRequest(data):
    lines = data.split(b'\r\n')


sock = socket(AF_INET, SOCK_STREAM) #IPv4 and TCP
sock.bind(("localhost",8432))
sock.listen()

while True:
    connsock, addr = sock.accept()
    print("connection from", addr)

    data = connsock.recv(1024)
    response = "request received!"

    
    #lines = data.splitlines(b'\r\n')
    #uri = lines[0].split(b" ").strip('/')
    #print(uri)



    #response_line = b"HTTP/1.1 200 OK\r\n\r\n"
    
    #with open(uri, 'rb') as f:
    #    response_body = f.read()

    #headers = b"".join([
    #    b"Content-Type: text/html\r\n"
    #    b"Content-Length: ", len(response_body), "\r\n\r\n"
    #])

    #response = b"".join([response_line, headers, response_body])

# handle data, make response 
    
    connsock.send(response)
    connsock.close()
