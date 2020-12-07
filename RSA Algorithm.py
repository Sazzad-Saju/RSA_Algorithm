# RSA Algorithm
# By Sazzad Saju
# CSE, HSTU
#
# Description: KeyGenerator program creates public_key (n,e) and
# private_key (p,q). This RSA program will work for small primes
# to big primes and generate encrypted string in HEX. Symmetric-
# key should be encrypted using RSA before transmiting on online.
import pyperclip

def ConvertToInt(message):
    grd = 1
    num = 0
    message = message[::-1]
    for i in range(0, len(message), +1):
        num = num + ord(message[i]) * grd
        grd *= 256
    return num

def mod_ex(b, k, m):
    i = 1
    j = 0
    while (j <= k):
        b = (b * i) % m
        i = b
        j += 1
    return b

def PowMod(b, e, m):
    bin_e = bin(e)
    bin_e = bin_e[::-1]
    ln = len(bin_e)
    result = 1
    for i in range(0, ln - 2, +1):
        if (bin_e[i] == '1'):
            result *= mod_ex(b, i, m)
    return result % m

def Encrypt(message, modulo, e):
    cytxt = ""
    temp = modulo // 256
    per_char = 0
    while (temp != 0):
        temp = temp // 256
        per_char += 1
    cyln = pow(256, per_char)
    cyln = len(str(cyln)) + 1
    s = message
    for i in range(0, len(message), +per_char):
        s1 = s[:per_char]
        b = ConvertToInt(s1)
        cytxt1 = str(PowMod(b, e, modulo))
        if (len(cytxt1) < cyln):
            while ((cyln - len(cytxt1) > 0)):
                cytxt1 = "0" + cytxt1
            cytxt += cytxt1
        else:
            cytxt += cytxt1
        s = s[per_char:]
    to_i = int(cytxt)
    to_h = '%X' % to_i
    hex_cytxt = str(to_h)
    return hex_cytxt

def eea(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        return (gcd, t, s)

def InvertModulo(e, phi):
    gcd, s, _ = eea(e, phi)
    if (gcd != 1):
        return None
    else:
        return s % phi

def ConvertToStr(num):
    st = ""
    while (num != 0):
        temp = num % 256
        st += chr(temp)
        chr(temp)
        num = num - temp
        num = num // 256
    st = st[::-1]
    return st

def Decrypt(ciphertext,modulo, e):
    with open('private_key', 'r') as f:
        p = f.readline()
        p = int(p[:-1])
        q = int(f.readline())
    to_i = int(ciphertext, 16)
    ciphertext = str(to_i)
    phi = (p - 1) * (q - 1)
    d = InvertModulo(e, phi)
    temp = modulo // 256
    per_char = 0
    while (temp != 0):
        temp = temp // 256
        per_char += 1
    cyln = pow(256, per_char)
    cyln = len(str(cyln)) + 1
    while (len(ciphertext) % cyln != 0):
        ciphertext = "0" + ciphertext
    s = ciphertext
    m = ""
    for i in range(0, len(ciphertext), +cyln):
        s1 = s[:cyln]
        b = int(s1)
        m += ConvertToStr(PowMod(b, d, modulo))
        s = s[cyln:]
    return m


with open('public_key','r') as f:
    modulo = f.readline()
    modulo = int(modulo[:-1])
    e = int(f.readline())
print("1) Encryption\n2) Decryption\n")
indicator = input("Enter Your Choice: ")
if(indicator=="1"):
    Message = input("Enter Message: ")
    ciphertext = Encrypt(Message, modulo, e)
    print("Ciphertext: {}".format(ciphertext))
    pyperclip.copy(ciphertext)
    spam = pyperclip.paste()
    print("Ciphertext is copped to clipboard!")
elif(indicator == "2"):
    ciphertext = input("Enter Ciphertext: ")
    message = Decrypt(ciphertext, modulo, e)
    print("Message: {}".format(message))