""" Caspar's

██████╗░░██████╗░█████╗░
██╔══██╗██╔════╝██╔══██╗
██████╔╝╚█████╗░███████║
██╔══██╗░╚═══██╗██╔══██║
██║░░██║██████╔╝██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
"""
import math
import random
from random import getrandbits

MESSAGE = 'hello'
BITS = 8

# generate random number of l bits
def rand_bits(l: int) -> int:
    # random bits
    p = getrandbits(l)
    return p

# -- TODO: replace with miller rabin
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

# create prime candidate & check if prime of length l bits
def make_primes(l: int) -> int:
    p = rand_bits(l)
    q = rand_bits(l)
    while is_prime(p) == False:
        p = rand_bits(l)
    while is_prime(q) == False and p != q:
        q = rand_bits(l)
    return p, q

# return number between 1 & m that is coprime with both m & n
def random_coprime(m: int) -> int:
    a = random.randint(2, m - 1)
    while math.gcd(a, m) != 1:
        a = random.randint(2, m - 1)
    return a

# compute keys
def generate_keys() -> dict:
    """
    p & q -> prime
    p != q
    """
    p, q = make_primes(BITS)
    # p = 2
    # q = 7 
    
    n = p * q
    # len/amount of non-common factors between 1 and n
    m = (p-1) * (q-1)

    # find the ENCRYPTION key
    """ requirements:
    random int between 1 and m (exclusive)
    coprime to m
    """
    a = random_coprime(m)

    # find the DECRYPTION key
    """ requirements:
    a * d % m = 1
    """
    # self-recursion until d != a
    d = pow(a, -1, m)
    if d == a:
        return generate_keys()
    # requirement met first try
    else:
        return {
            'encryption': (a, n, d),
            'private': m
        }

keys = generate_keys()
print(keys)