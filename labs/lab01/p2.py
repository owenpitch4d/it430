import sys

try:
    f = open(sys.argv[1], "rb")
except: 
    print("File not found!")
    exit(0)

length = 0
binary_file = f.read(16) # take 16 bytes at a time
length += len(binary_file)
count = 0 #hex counter

while binary_file:
    hex_column1 = " ".join([f"{i:02x}" for i in binary_file[0:8]])
    hex_column2 = " ".join([f"{i:02x}" for i in binary_file[8:]])
    hex_column = hex_column1 + " " + hex_column2 #space inbetween hex columns
    
    text = "".join([chr(i) if chr(i).isprintable() else "." for i in binary_file])

    print(f"{count:08x}  {hex_column:<48}  |{text}|")
    count += 16
    binary_file = f.read(16)
    length += len(binary_file)

print(f"{length:08x}")
f.close()
