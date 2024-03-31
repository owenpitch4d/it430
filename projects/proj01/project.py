#!/usr/bin/python3
# project.py
# Owen Pitchford
# 255076
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad

# read in_plain_file, encrypt the data, and store the ciphertext in out_cipher_file
def encrypt_ecb(in_plain_file, out_cipher_file, key):
    with open(in_plain_file, "rb") as f:
        b_file = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    with open(out_cipher_file, "wb") as f:
        f.write(cipher.encrypt(pad(b_file, 16)))
    
    return out_cipher_file

# read in_cipher_file, decrypt the ciphertext, and store the plaintext in out_plain_file
def decrypt_ecb(in_cipher_file, out_plain_file, key):
    with open(in_cipher_file, "rb") as f:
        cipher_text = f.read()
    
    cipher = AES.new(key, AES.MODE_ECB)

    with open(out_plain_file, "wb") as f:
        f.write(unpad(cipher.decrypt(cipher_text), 16))
    
    return out_plain_file

    
# read normal_bmp_file and in_cipher_file, fix the header in the ciphertext and
# store the results in out_cipher_bmp_file
def fix_bmp_header(normal_bmp_file, in_cipher_file, out_cipher_bmp_file):
    with open(normal_bmp_file, "rb") as f:
        header = f.read(54)
    
    with open(in_cipher_file, "rb") as f:
        data = f.read()[54:]
    
    with open(out_cipher_bmp_file, "wb") as f:
        f.write(header + data)
    
    return out_cipher_bmp_file

def encrypt_cbc(in_plain_file, out_cipher_file, key, iv):
    with open(in_plain_file, "rb") as f:
        b_file = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(out_cipher_file, "wb") as f:
        f.write(cipher.encrypt(pad(b_file, 16)))
    
    return out_cipher_file

def decrypt_cbc(in_cipher_file, out_plain_file, key, iv):
    with open(in_cipher_file, "rb") as f:
        cipher_text = f.read()
    
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)

        with open(out_plain_file, "wb") as f:
            f.write(unpad(cipher.decrypt(cipher_text), 16))
        
        return out_plain_file
    except (ValueError, KeyError):
        print("Incorrect Decryption")

def encrypt_ctr(in_plain_file, out_cipher_file, key, ctr):
    with open(in_plain_file, "rb") as f:
        b_file = f.read()

    cipher = AES.new(key, AES.MODE_CTR, nonce=ctr[0:8], initial_value=ctr[8:])

    with open(out_cipher_file, "wb") as f:
        f.write(cipher.encrypt(b_file))
    
    return out_cipher_file

def decrypt_ctr(in_cipher_file, out_plain_file, key, ctr):
    with open(in_cipher_file, "rb") as f:
        cipher_text = f.read()
    
    try:
        cipher = AES.new(key, AES.MODE_CTR, nonce=ctr[0:8], initial_value=ctr[8:16])

        with open(out_plain_file, "wb") as f:
            f.write(cipher.decrypt(cipher_text))
        
        return out_plain_file
    except (ValueError, KeyError):
        print("Incorrect Decryption")

def pad2(data):
    blk_size = 16

    while(len(data) >= blk_size): blk_size += 16

    pad_len = blk_size - len(data)

    return data.ljust(blk_size, pad_len.to_bytes(1, "little"))

def unpad2(data):
    if(len(data) % 16 != 0):
        print("padding error!")
        return None
    
    pad = data[-1]
    count = 0

    for byte in data[len(data)-pad:]:
        if(byte == pad): count += 1

    if(count == pad): return data[:-pad]
    else:
        print("padding error!") 
        return None

def part4(pt, ct, target):
    pt = int.from_bytes(bytes.fromhex(pt), 'little')
    ct = int.from_bytes(bytes.fromhex(ct), 'little')
    t = int.from_bytes(bytes.fromhex(target), 'little')

    #key = (pt^ct).to_bytes(max(sys.getsizeof(pt), sys.getsizeof(ct)), 'little')
    key = (pt^ct)

    m = (t^key).to_bytes(max(sys.getsizeof(t), sys.getsizeof(key)), 'little')

    return m.decode()

def part5(in_cipher_file):
    with open(in_cipher_file, "rb") as f:
        cipher_text = f.read()
    
    cipher_text = bytearray(cipher_text)
    cipher_text[70] = 0


    with open(in_cipher_file, "wb") as f:
        f.write(cipher_text)

    return in_cipher_file
    

