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

# check if n of (k-bits) is a prime # TODO: replace with miller rabin
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

# return number between 1 & m that is coprime with both m & n
def find_coprime(m, n):
    for i in range(2, m):
        if math.gcd(i, m) == 1 & math.gcd(i, n) == 1:
            return i

# compute keys
def make_keys() -> dict:
    p = 2#make_prime(BITS)
    q = 7#make_prime(BITS)
    
    n = p * q
    m = (p-1) * (q-1)

    a = find_coprime(m, n)
    return {
        'private': m,
        'public': (a, n)
    }

d = make_keys()
print(d)