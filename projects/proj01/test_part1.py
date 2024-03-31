#!/usr/bin/python3
# test_part1.py

from project import *

key = bytes.fromhex("00112233445566778899aabbccddeeff")
encrypt_ecb("pic_original.bmp", "prj_ecb.bin", key)
decrypt_ecb("prj_ecb.bin", "prj_dec.bmp", key)
fix_bmp_header("pic_original.bmp", "prj_ecb.bin", "prj_ecb.bmp")