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

    key = (pt^ct)

    m = (t^key).to_bytes(max(sys.getsizeof(t), sys.getsizeof(key)), 'little')

    return m.decode()

def part6(in_cipher_file):
    with open(in_cipher_file, "rb") as f:
        cipher_text = f.read()
    
    corrupt_text = bytearray(cipher_text)
    corrupt_text[70] = 0
    
    with open(in_cipher_file, "wb") as f:
        f.write(corrupt_text)

    return in_cipher_file
    

def part5(iv1, iv2):
    yes = int.from_bytes(pad(b'Yes', 16), "big") #pad yes message and convert to int
    no = int.from_bytes(pad(b'No', 16), "big") #pad no messasge and convert to int

    #convert IVs to int
    iv1 = int(iv1, 16)
    iv2 = int(iv2, 16)

    #xor pt with original iv to get what went into encryption box
    yes = yes^iv1
    no = no^iv1

    #get m1 by xor with new iv
    m1_yes = hex(yes^iv2)        
    m1_no = hex(no^iv2)        
    
    print("manipulated yes = " + m1_yes)
    print("manipulated no = " + m1_no)

iv1 = "890cc7d758854e4c2339e490bf31b4c4"
#iv2 = "461042508b8152abac76f4ce802e64df"
iv2 = "3666689ef678a1bb09b4bc0a7103bf72"
part5(iv1, iv2)


