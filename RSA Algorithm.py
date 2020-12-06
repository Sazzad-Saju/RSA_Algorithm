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

def Encrypt(message, modulo, exponent):
    cytxt = ""
    w = modulo // 256
    letter = 0
    while (w != 0):
        w = w // 256
        letter += 1
    cyln = pow(256, letter)
    cyln = len(str(cyln)) + 1
    s = message
    for i in range(0, len(message), +letter):
        s1 = s[:letter]
        Con = ConvertToInt(s1)
        cytxt1 = str(PowMod(Con, exponent, modulo))
        if (len(cytxt1) < cyln):
            while ((cyln - len(cytxt1) > 0)):
                zr = "0"
                cytxt1 = zr + cytxt1
            cytxt += cytxt1
        else:
            cytxt += cytxt1
        s = s[letter:]
    return cytxt

def eea(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        return (gcd, t, s)

def InvertModulo(e, r):
    gcd, s, _ = eea(e, r)
    if (gcd != 1):
        return None
    else:
        return s % r

def ConvertToStr(m):
    st = ""
    while (m != 0):
        temp = m % 256
        st += chr(temp)
        chr(temp)
        m = m - temp
        m = m // 256
    st = st[::-1]
    return st

def Decrypt(ciphertext, p, q, exponent):
    modulo = p * q
    n = (p - 1) * (q - 1)
    d = InvertModulo(exponent, n)
    w = modulo // 256
    letter = 0
    while (w != 0):
        w = w // 256
        letter += 1
    cyln = pow(256, letter)
    cyln = len(str(cyln)) + 1
    s = ciphertext
    m = ""
    for i in range(0, len(ciphertext), +cyln):
        s1 = s[:cyln]
        Con = int(s1)
        m += ConvertToStr(PowMod(Con, d, modulo))
        s = s[cyln:]
    return m


p = 57704576143051
q = 838744063
e = 2237
modulo = p * q
ciphertext = Encrypt("Down the Rabbit-Hole", modulo, e)
print(ciphertext)
message = Decrypt(ciphertext, p, q, e)
print(message)