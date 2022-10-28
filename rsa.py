"""
______  _____  ___  
| ___ \/  ___|/ _ \ 
| |_/ /\ `--./ /_\ |
|    /  `--. \  _  |
| |\ \ /\__/ / | | |
\_| \_|\____/\_| |_/

"""
import math
from random import randrange, getrandbits

# generate random prime number of length l
def rand_bits(l: int) -> int:
    # random bits
    p = getrandbits(l)

    return p

# check if n of (k-bits) is a prime
def is_prime(n: int, k=32) -> bool:
    # check if even
    if n % 2 == 0:
        return False
    # test each odd num from 3 to sqrt(n)
    for i in range(3, math.ceil(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

print(rand_bits(265))

# create prime candidate & check if prime


# compute keys
