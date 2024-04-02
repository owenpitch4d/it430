#!/usr/bin/python3
# test_part5.py

import project

key = bytes.fromhex("00112233445566778899aabbccddeeff")
iv = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

project.encrypt_ecb("pic_original.bmp", "prj_ecb.bin", key)

project.encrypt_cbc("pic_original.bmp", "prj_cbc.bin", key, iv)
#project.decrypt_cbc("prj_cbc.bin", "prj_cbc_dec.bmp", key, iv)

ctr = iv
project.encrypt_ctr("pic_original.bmp", "prj_ctr.bin", key, ctr)
#project.decrypt_ctr("prj_ctr.bin", "prj_ctr_dec.bmp", key, ctr)

project.part5("prj_ecb.bin")
project.part5("prj_cbc.bin")
project.part5("prj_ctr.bin")


project.decrypt_ecb("prj_ecb.bin", "prj_dec1.bmp", key)
project.fix_bmp_header("pic_original.bmp", "prj_ecb.bin", "prj_ecb.bmp")

project.decrypt_cbc("prj_cbc.bin", "prj_cbc_dec1.bmp", key, iv)

project.decrypt_ctr("prj_ctr.bin", "prj_ctr_dec1.bmp", key, ctr)