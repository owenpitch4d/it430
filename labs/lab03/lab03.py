import struct
def showpkts(data):
    data = data[24:] #remove global header
    
    while(data):
        #remove excess header but leave the size port
        data = data[12:]
        print("data:")

        #find packet length
        pkt_len = int.from_bytes(data[0:4], "little")
        
        data = data[4:] #get rid of length

        #convert only the first packet to hex
        tempData = ([f"{i:02x}" for i in data[0:pkt_len]])
        
        for index, element in enumerate(tempData, start=1):
            print(element, end='')
            if index%16==0:
                print("")
            elif index%8==0:
                print(" ", end='')
            else:
                print(" ", end='')
        data = data[pkt_len:]
        print("\n")
    

    #data = open("two.pcap", "rb").        data = data[12:]read()
    #showpkts(data)
        
def showpkts_Eth(data):
    data = data[24:] #remove global header
    
    while(data):
        #remove excess header but leave the size port
        data = data[12:]
        print("data:")

        #find packet length
        pkt_len = int.from_bytes(data[0:4], "little")
        
        data = data[4:] #get rid of length

        #convert only the first packet to hex
        tempData = ([f"{i:02x}" for i in data[0:pkt_len]])

        print("Dst-MAC=", getAdr(tempData))
        tempData = tempData[6:]

        print("Src-MAC=", getAdr(tempData))
        tempData = tempData[6:]

        print("Type=", tempData[0] + " " + tempData[1])
        tempData = tempData[2:]

        for index, element in enumerate(tempData, start=1):
            print(element, end='')
            if index%16==0:
                print("")
            elif index%8==0:
                print(" ", end='')
            else:
                print(" ", end='')
        data = data[pkt_len:]
        print("\n")
    
def getAdr(data):
    dstMac = ""
    for index, element in enumerate(data[0:6], start = 1):
        dstMac += element
        if(index != 6):
            dstMac += ":"
    
    return dstMac
    #data = open("two.pcap", "rb").        data = data[12:]read()
    #showpkts(data)