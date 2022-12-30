""" Caspar's

██████╗░░██████╗░█████╗░
██╔══██╗██╔════╝██╔══██╗
██████╔╝╚█████╗░███████║
██╔══██╗░╚═══██╗██╔══██║
██║░░██║██████╔╝██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
"""
import sys
import math
import random
import time
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
    while is_prime(q) == False:
        q = rand_bits(n)

    if p == q:
        make_primes()
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
    b = pow(a, -1, m)

    if b == a:
        return generate_keys()
    # else when requirement met first try
    else:
        # write keys to file
        with open('keys.txt', 'w') as f:
            # public (n, a), private (n, b)
            keys = [str(n), str(a), str(b)]
            f.write('\n'.join(keys))
        return

# takes keys plain text; returns encrypted str
def encrypt(plain: str) -> str:
    # read keyfile
    with open('keys.txt') as f:
        lines = f.readlines()
        n = int(lines[0])
        a = int(lines[1])

    cipher = ''
    # encrypt ascii values of each char
    for c in plain:
        cipher += chr((ord(c) ** a) % n)

    # encode str to bytes and then base64
    cipher = cipher.encode('utf-8')
    cipher = base64.b64encode(cipher).decode()

    return cipher

# takes cipher text; returns decrypted str
def decrypt(cipher: str) -> str:
    # read keyfile
    with open('keys.txt') as f:
        lines = f.readlines()
        n = int(lines[0])
        b = int(lines[2])

    # decode from base64 to bytes and then str
    cipher = base64.b64decode(cipher.encode())
    cipher = cipher.decode('utf-8')
    
    # decrypt ascii values of each char
    plain = ""
    for c in cipher:
        plain += chr((ord(c) ** b) % n)
    
    return plain

# applies the rsa pipeline to a string
# 0 -> encrypt ; 1 -> decrypt
def rsa(s: str, mode: int) -> str:
    # start timer
    st = time.time()

    # encrypt
    if mode == 0:
        text = encrypt(s)
    # decrypt
    elif mode == 1:
        text = decrypt(s)

    # return text and time
    return (text, time.time() - st)

# read command line arguments
args = sys.argv
if args[1] == '-n':
    # generate new keys
    generate_keys()
    print("generated new keys!")
elif args[1] == '-e':
    try:
        message = args[2]
    except IndexError:
        print('please enter a message!')
        sys.exit()
    # ENCRYPT to ciphertext
    c = rsa(message, 0)
    print(f'encrypted {message} to\n{c[0]}\n--------\nfinished in {round(c[1], 4)} s')

elif args[1] == '-d':
    try:
        message = args[2]
    except IndexError:
        print('please enter a message!')
        sys.exit()
    # DECRYPT to plain text:
    p = rsa(message, 1)
    print(f'decrypted {message} to\n{p[0]}\n--------\nfinished in {round(p[1], 4)} s')
