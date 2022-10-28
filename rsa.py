""" Caspar's
______  _____  ___  
| ___ \/  ___|/ _ \ 
| |_/ /\ `--./ /_\ |
|    /  `--. \  _  |
| |\ \ /\__/ / | | |
\_| \_|\____/\_| |_/

"""
import math
from random import getrandbits

MESSAGE = 'hello'
BITS = 8

# generate random number of l bits
def rand_bits(l: int) -> int:
    # random bits
    p = getrandbits(l)
    return p

# check if n of (k-bits) is a prime
def is_prime(n: int) -> bool:
    # check if even
    if n % 2 == 0:
        return False
    # test each odd num from 3 to sqrt(n)
    for i in range(3, math.ceil(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

# create prime candidate & check if prime
def make_prime(l: int) -> int:
    p = rand_bits(l)
    while is_prime(p) == False:
        p = rand_bits(l)
    return p

# compute keys
def make_keys() -> dict:
    p = 5#make_prime(BITS)
    q = 11#make_prime(BITS)
    n = p * q

    m = (p-1) * (q-1)
    a = 7 # TODO: generate a coprime of m
    return {
        'private': m,
        'public': (n, a)
    }

d = make_keys()
print(d)
