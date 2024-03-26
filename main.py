import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modinv: {0} has no multiplicative inverse mod {1}'.format(a, m))
    else:
        return x % m

def decrypt(c, e, n):
    d = modinv(e, n)
    m = pow(c, d, n)
    return m

c = 40378206529498051531945975088384209929958842890390583399916702446047201280545
e = 1
n = 50374326529498099531945975088384209929958842890390583399916702446047201280545

m = decrypt(c, e, n)
print(m)