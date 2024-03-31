import sys
C = int.from_bytes(bytes.fromhex("a3890567e9cb50d0754627"), 'little')
K = int.from_bytes(bytes.fromhex("ebec690b86eb07bf072a43"), 'little')

M = (C ^ K).to_bytes(max(sys.getsizeof(C), sys.getsizeof(K)), 'little')

print(M.decode())



M = int.from_bytes(b'IT430 Rocks!', 'little')
C = int.from_bytes(b'\xbeM\x90\x9c{}a/OVW\x93', 'little')

K = (M ^ C)
#.to_bytes(max(sys.getsizeof(C), sys.getsizeof(M)), 'little')

C = int.from_bytes(b'\xb0v\x84\xe1*+Ja\r\x1c\x05\x93', 'little')

M = (C ^ K).to_bytes(max(sys.getsizeof(C), sys.getsizeof(K)), 'little')

print(M.decode())

