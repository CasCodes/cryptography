"""
Simple cipher using the Fibonacci sequence
"""

# get input
text = input('enter text: ').lower()

# output fibonacci num of n
def fib(n: int) -> int:
    if n == 0:
        return 0
    # Check if n is 1,2
    elif n == 1 or n == 2:
        return 1 
    else:
        return fib(n-1) + fib(n-2)

def encrypt(text: str) -> str:
    cipher = ""
    for i in range(len(text)):
        if text[i].isalpha():
            # get alphabetic position of char
            pos = ord(text[i]) - ord('a')

            # get fib value of alphabetic pos of char i
            cipher += str(fib(pos))
            cipher += " "
        else:
            cipher += text[i]
    return cipher

print(encrypt(text))
