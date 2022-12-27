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
import base64

BITS = 8

# generate random number of n bits
def rand_bits(n: int) -> int:
    return random.randrange(2**(n-1)+1, 2**n-1)

# check if n is a prime
def is_prime(n: int) -> bool:
    # check if even
    if n % 2 == 0:
        return False
    # test each odd num from 3 to sqrt(n)
    for i in range(3, math.ceil(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

# create two unique random primes of size n
def make_primes(n: int) -> int:
    p = rand_bits(n)
    q = rand_bits(n)

    while is_prime(p) == False:
        p = rand_bits(n)
    while is_prime(q) == False and p != q:
        q = rand_bits(n)
    return p, q

# return number between 1 & m that is coprime with m
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
    a = random_coprime(m)

    """ requirements:
    a * d % m = 1
    """
    # modular inverse
    # self-recursion until d != a
    d = pow(a, -1, m)
    if d == a:
        return generate_keys()
    # else when requirement met first try
    else:
        return {
            "private": (n, d),
            "public":  (n, a)
        }

# takes keys plain text; returns encrypted str
def rsa_encrypt(public_key: tuple[int, int], plain: str) -> str:
    n, a = public_key

    cipher = ''
    # encrypt ascii values of each char
    for c in plain:
        cipher += chr((ord(c) ** a) % n)
    
    # encode str to bytes and then base64
    cipher = cipher.encode('utf-8')
    cipher = base64.b64encode(cipher).decode()

    return cipher

# takes keys and cipher text; returns decrypted str
def rsa_decrypt(private_key: tuple[int, int], cipher: str) -> str:
    # read key from file
    n, d = private_key

    # decode from base64 to bytes and then str
    cipher = base64.b64decode(cipher.encode())
    cipher = cipher.decode('utf-8')
    
    # decrypt ascii values of each char
    plain = ""
    for c in cipher:
        plain += chr((ord(c) ** d) % n)
    print(plain)
    return plain
