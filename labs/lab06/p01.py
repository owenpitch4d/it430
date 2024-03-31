#!/usr/bin/python3
# p01.py
from socket import *
import struct

raw_socket = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)

udp_payload = b"alex and owen are awesome"
udp_header = struct.pack(">HHHH", 44195, 9000, 8 + len(udp_payload), 0) #my HS lunch number
ip_payload = udp_header + udp_payload

#ip_header
version = 4
ihl = 5

version_ihl = (version << 4) | ihl
type_of_service = 0
total_length = 20 + len(ip_payload)
ip_header = struct.pack(">BBH", version_ihl, type_of_service, total_length)
ip_header += struct.pack(">HH", 12345, 0)
ttl = 20
protocol = 17
checksum = 0
ip_header += struct.pack(">BBH", ttl, protocol, checksum)

ip_header += struct.pack(">BBBB", 6, 17, 11, 26) #our birthdays
ip_header += struct.pack(">BBBB", 192, 168, 172, 5) #it430b
ip_pkt = ip_header + ip_payload

addr = ("192.168.172.5", 9000)
raw_socket.sendto(ip_pkt, addr)