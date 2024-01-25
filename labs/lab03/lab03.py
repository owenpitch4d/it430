import struct
def showpkts(data):
    data = data[36:] #remove global header
    
    pkt_len = int.from_bytes(data[0:4], "little")
    data = data[4:]
    while(data):
        hex_column1 = " ".join([f"{i:02x}" for i in data[0:8]])
        hex_column2 = " ".join([f"{i:02x}" for i in data[8:16]])
        hex_column = hex_column1 + "  " + hex_column2
        print(f"{hex_column:<49}")
        data = data[16:]

            



data = open("two.pcap", "rb").read()
showpkts(data)