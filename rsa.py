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
import time
import base64

BITS = 8

# generate random number of n bits
def rand_bits(n: int) -> int:
    # random bits
    return random.randrange(2**(n-1)+1, 2**n-1)

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

# create prime candidate of size n & check if prime
def make_primes(n: int) -> int:
    p = rand_bits(n)
    q = rand_bits(n)

    while is_prime(p) == False:
        p = rand_bits(n)
    while is_prime(q) == False and p != q:
        q = rand_bits(n)
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
def encrypt(public_key: tuple[int, int], plain: str):
    n, a = public_key

    cipher = ''
    # loop over byte string and encrypt
    for c in plain:
        cipher += chr((ord(c) ** a) % n)
    
    # encode str to bytes and then base64
    cipher = cipher.encode('utf-8')
    cipher = base64.b64encode(cipher).decode()

    return cipher

# takes keys and encrypted int; returns decrypted int
def decrypt(private_key: tuple[int, int, int], cipher: str):
    # read key from file
    n, d = private_key

    # decode from base64 to bytes and then str
    cipher = base64.b64decode(cipher.encode())
    cipher = cipher.decode('utf-8')
  
    plain = ""
    for c in cipher:
        plain += chr((ord(c) ** d) % n)
    return plain


def rsa(s: str):
    # start timer
    st = time.time()

    # load keys
    keys = generate_keys()

    cipher = encrypt(keys["public"], s)
    print(cipher)

    # decrypt encrypted string
    plain = decrypt(keys["private"], cipher)

    # print time
    print(f"{plain} \n--------\ntime: {time.time() - st}")

s= "Hi"
rsa(s)


# TODO: read / write key file