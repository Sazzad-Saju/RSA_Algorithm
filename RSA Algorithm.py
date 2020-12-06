import sys, threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

def ConvertToInt(message_str):
    res = 0
    for i in range(len(message_str)):
        res = res*256 + ord(message_str[i])
    return res

def ConvertToStr(n):
    res = ""
    while n>0:
        res += chr(n%256)
        n //= 256
    return res[::-1]

def PowMod(a,n,mod):
    if n==0:
        return 1 % mod
    elif n==1:
        return a % mod
    else:
        b = PowMod(a, n//2, mod)
        b = b * b % mod
        if n%2 == 0:
            return b
        else:
            return b * a % mod

def ExtendedEuclid(a,b):
    if b == 0:
        return (1,0)
    (x,y) = ExtendedEuclid(b, a%b)
    k = a // b
    return (y,x- k * y)

def InvertModulo(a,n):
    (b,x) = ExtendedEuclid(a,n)
    if b < 0:
        b = (b % n + n) % n
    return b

def Encrypt(message, modulo, exponent):
    s = ConvertToInt(message)
    return PowMod(s,exponent, modulo)

def Decrypt(ciphertext, p, q, exponent):
    n = (p-1) * (q-1)
    d = InvertModulo(exponent, n)
    return ConvertToStr(PowMod(ciphertext,d,p * q ))

p = 779849711281
q = 748173698927
e = 1018651

n = p*q
message = "Down the r"
ciphertext = Encrypt(message, n, e)
print(ciphertext)
message = Decrypt(ciphertext,p,q,e)
print(message)