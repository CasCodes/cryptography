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
import time

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
    """ requirements
    p & q -> prime
    p != q
    """
    p, q = make_primes(BITS)

    n = p * q
    # amount of non-common factors between 1 and n
    m = (p-1) * (q-1)

    """ requirements:
    random int between 1 and m (exclusive)
    coprime to m
    """
    # TODO catch ValueError for randrange
    a = random_coprime(m)

    """ requirements:
    a * d % m = 1
    """
    # modular inverse
    # self-recursion until d != a
    d = pow(a, -1, m)
    if d == a:
        return generate_keys()
    # requirement met first try
    else:
        return {
            "private": (n, d),
            "public":  (n, a)
        }

# takes keys and int encoded plain text; returns encrypted int
def encrypt(public_key: tuple[int, int], plain: int) -> int:
    n, a = public_key
    cipher = (plain ** a) % n
    return cipher 

# takes keys and encrypted int; returns decrypted int
def decrypt(private_key: tuple[int, int, int], cipher: int) -> int:
    n, d = private_key
    plain = (cipher ** d) % n
    return plain

def rsa(s: str):
    st = time.time()

    keys = generate_keys()
    s = s.encode("utf-8") 
    # encrypt
    cipher = []
    for c in s:
        cipher.append(encrypt(keys["public"], c))
    
    cip = "".join(chr(i) for i in cipher)
    print(cip)
    
    # decrypt
    plain = []
    for c in cipher:
        plain.append(decrypt(keys["private"], c))

    print(cipher, plain)
    text = ""
    for i in plain:
        text += chr(i)
    print(f"{text} \n--------\n{time.time() - st}")

s= "hello world"
rsa(s)
