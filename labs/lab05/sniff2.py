#!/usr/bin/python3
# serv_udp.py
from socket import *
import select
import sys

def getMAC(data2):

    mac = ""
    for index, element in enumerate(data2[0:6], start = 0):
        if(index != 5):
            mac = mac + data2[index] + ":"
        else:
            mac = mac + data2[index]
    return mac

def getIP(data1):

    IP = ""
    for index, element in enumerate(data1[0:4], start = 0):
        if(index != 3):
            IP = IP + str(int(data1[index], 16)) + "."
        else:
            IP = IP + str(int(data1[index], 16))
    return IP

def getPort(data3):
    
    tempPort = data3[0] + data3[1]

    return int(tempPort, 16)

def getMsg(data4):
    msg = ""
    for element in data4:

        #To make the \n not appear as an actual newline
        if(int(element, 16) == 10):
            msg+= "\\n"
        else:
            msg += chr(int(element, 16))
    return msg

ETH_P_ALL = 0x0003
raw_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))

while True:

    (data, addr) = raw_socket.recvfrom(1024)

    typey = (data[12:14]).hex()
    length = int.from_bytes(data[16:18], 'big')
    protocol = data[23]

    #the +14 accounts for the ethernet header
    tempData = ([f"{i:02x}" for i in data[0:length+14]])

    #Need to check the ports before the loop to match up 9000
    dstPort = getPort(tempData[36:38])
    srcPort = getPort(tempData[34:36])



    if(typey == "0800" and protocol == 17 and (dstPort == 9000 or srcPort == 9000)):

        dstMAC = getMAC(tempData[0:6])
        srcMAC  = getMAC(tempData[6:12])

        dstIP = getIP(tempData[30:34])
        srcIP = getIP(tempData[26:30])

        msg = getMsg(tempData[42:length+14])

        print(f"src: {srcIP}({srcPort}) [{srcMAC}]")
        print(f"dst: {dstIP}({dstPort}) [{dstMAC}]")
        print(f"b'{msg}'")



