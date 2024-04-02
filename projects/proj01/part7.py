#!/usr/bin/python3
# part7.py

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import *
import Cryptodome.Random as Random
from Cryptodome.Random import random
from project import *

# Two messages
M = [
b"Don't use ECB. It's not IND-CPA secure",
b"Show that CBC is not IND-CCA secure!!!"
]

# Choose a random bit b
b = random.getrandbits(1) 
pt = M[b]    # plaintext 

# Random key and iv
key = Random.get_random_bytes(16)
iv = Random.get_random_bytes(16)

# CBC encryption
aes = AES.new(key, AES.MODE_CBC, iv)
ct = aes.encrypt(pad(pt,AES.block_size))

# start of the game : show the ciphertext
print("The target ciphertext is")
print("iv:", iv.hex())
print("ct:", ct.hex())
print()


# give the chance to figure things out 
while True:

  s = input("\n=============\nMenu: 0 (encrypt), 1 (decrypt), 2 (open): ")

  try: 
    menu = int(s)

    if menu == 0: 
      m = input("msg to encrypt in a hexstring format: ")
      m = bytes.fromhex(m)
      iv1 = Random.get_random_bytes(16)
      aes = AES.new(key, AES.MODE_CBC, iv1)
      ct1 = aes.encrypt(pad(m,AES.block_size))
      
      print("iv:", iv1.hex())
      print("ct:", ct1.hex())

    elif menu == 1: 
      iv1 = input("iv (in hexstring): ")
      iv1 = bytes.fromhex(iv1)
      if len(iv1) != 16:
        print("iv should be 16 bytes long")
        continue

      ct1 = input("ct (in hexstring): ")
      ct1 = bytes.fromhex(ct1)

      if iv1 == iv and ct1 == ct:
        print("Cannot decrypt the target ciphertext!")
        continue

      aes = AES.new(key, AES.MODE_CBC, iv1)
      m = unpad(aes.decrypt(ct1),AES.block_size)
      print("decryption is: ")
      print("   ", m) 

    elif menu == 2:
      break

  except: 
    print("Something went wrong")
    continue
  

# open the message
print("The message was: ", M[b])
