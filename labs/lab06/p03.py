#!/usr/bin/python3
# p03.py

import struct
import random
from socket import *

def calc_checksum(d):
  total = 0

  for i in range(0, len(d), 2):
      total += d[i]*256 + d[i+1]

  while total > 0xffff:
      total = (total >> 16) + (total & 0xffff)

  return total ^ 0xffff

#tcp_header
raw_socket = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)
src_port = random.randint(1, 65535)
sequence_number = random.randint(1,4294967295)#2^32 - 1
ACK_number = 0
tcp_header = struct.pack(">HHII", src_port, 9000, sequence_number, ACK_number)
tcp_header += b'\x50\x02\xfa\xf0' #data offset, SYN flag, window size

src_ip = struct.pack(">BBBB", 192, 168, 172, 6) #source ip
dst_ip = struct.pack(">BBBB", 192, 168, 172, 5) #dest

chksum = calc_checksum(src_ip + dst_ip + struct.pack(">BBH", 0, 6, 20) + tcp_header)
tcp_header += struct.pack(">HH", chksum, 0)
#ip_header
version = 4
ihl = 5
version_ihl = (version << 4) | ihl
type_of_service = 0
total_length = 20 + len(tcp_header)
ip_header = struct.pack(">BBH", version_ihl, type_of_service, total_length)
ip_header += struct.pack(">HH", 12345, 0)
ttl = 20
protocol = 6
checksum = 0
ip_header += struct.pack(">BBH", ttl, protocol, checksum)
ip_header += src_ip
ip_header += dst_ip

ip_pkt = ip_header + tcp_header

addr = ("192.168.172.5", 9000)
raw_socket.sendto(ip_pkt, addr)
