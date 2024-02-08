def showpkts_IP(data):
    data = data[24:] #Get rid of global header
    
    while(data):
        #Get rid of excess packet header
        data = data[12:]

        #Find the packet length
        pkt_len = int.from_bytes(data[0:4], "little")
        
        #Get rid of that packet length
        data = data[4:]
        
        #Turn only that packet to hex
        tempData = ([f"{i:02x}" for i in data[0:pkt_len]])
        
        print("Dst-MAC=", getAdr(tempData))
        tempData= tempData[6:]
        print("Src-MAC=", getAdr(tempData))
        tempData= tempData[8:]
        
        verIHL= tempData[0]
        IHL = int(verIHL, 16)%16
        print("IHL=", IHL)
        tempData = tempData[2:]

        totalLength = int(tempData[0]+tempData[1], 16)
        print("Total Length=", totalLength) 
        tempData = tempData[2:]
        
        #junk    
        tempData = tempData[5:]
        protocol = int(tempData[0], 16)
        tempData = tempData[3:]

        print("Src-IP=", getIP(tempData))
        tempData = tempData[4:]
        print("Dst-IP=", getIP(tempData))
        tempData = tempData[4:]
        
        getData(tempData)
        data = data[pkt_len:]
        print('')

def getData(bigData):
    #Format the data properly
    print("data:")
    for index, element in enumerate(bigData, start=1):
        print(element, end='')
        #End line
        if index%16==0: print('')
        # middle speration
        elif index%8==0: print("  ", end='')
        #No change
        else: print(" ", end='')

def getIP(data2):
    IP = ""
    for index, element in enumerate(data2[0:4], start = 1):
        element = str(int(element, 16))
        IP = (IP + element)
        if(index != 4):
            IP = IP + "."
    return IP

def getAdr(data2):
    dstMac =""
    for index, element in enumerate(data2[0:6], start = 1):
        dstMac = (dstMac + element)
        if(index != 6):
            dstMac = dstMac + ":"
    return dstMac

def showpkts_TCP(data, ip1, ip2):
    #Get rid of global header
    data = data[24:]
    
    while(data):
        #Get rid of excess packet header
        data = data[12:]

        #Find the packet length
        pkt_len = int.from_bytes(data[0:4], "little")
        
        #Get rid of that packet length
        data = data[4:]
        
        #Turn only that packet to hex
        tempData = ([f"{i:02x}" for i in data[0:pkt_len]])
        tempData= tempData[23:]
        protocol = int(tempData[0], 16)
        
        #skip if not TCP 
        if(protocol != 6): 
            data = data[pkt_len:]
            continue
        
        tempData = tempData[3:]

        src_ip = getIP(tempData)
        tempData = tempData[4:]
        dst_ip = getIP(tempData)        
        tempData = tempData[4:]

        src_port = int(tempData[0] + tempData[1], 16)
        dst_port = int(tempData[2] + tempData[3], 16)
        
        offset = (int(tempData[12], 16) >> 4) * 4 #bit manipulation for offset
        flags = int(tempData[12][1] + tempData[13], 16)
        
        tempData = tempData[offset:]
        if(ip1 == src_ip and ip2 == dst_ip or ip1 == dst_ip and ip2 == src_ip):
           msg = bytes.fromhex(" ".join(tempData))
           if flags == 0x018:
               print(f"{src_ip}({src_port}) ->  {dst_ip}({dst_port}) :")
               print(f" {msg}")
           
        
        data = data[pkt_len:]
    

data = open("tcp.pcap", "rb").read()
showpkts_TCP(data, "192.168.172.4", "192.168.172.5")