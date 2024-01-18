# p3.py

def pr(a):
    print(f"dec: {a:d}\nhex: 0x{a:02x}\nbin: {a:08b}")


def zero_out_top(a, n):
    b = 0b0000000011111111
    c = (a << n) & b
    c = c >> n
    return c

def set_one_at(a, i):

    b = 0b0000000010000000
    c = (a << i) | b
    c = c >> i 
    return c

def set_zero_at(a, i):
    b = 0b1111111101111111
    c = (a << i) & b
    c = c >> i
    return c