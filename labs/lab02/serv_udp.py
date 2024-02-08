#!/usr/bin/python3
# serv_udp.py
from socket import *
import select
import sys

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("0.0.0.0",9000))
data, addr = sock.recvfrom(1024)
print("From ", addr, ":", data)

while True:
    socklist = [sock, sys.stdin]
    (r_sockets, w_sockets, e_sockets) = select.select(socklist, [], [])
    
    if sock in r_sockets:
        data,addr = sock.recvfrom(1024)
        if not data:
            break
        print(data.decode().strip())
    
    if sys.stdin in r_sockets:
        s = input()
        if s == "quit":
            break
        s = s.strip()
        s += '\n'
        sock.sendto(s.encode(), addr)
    
sock.close()