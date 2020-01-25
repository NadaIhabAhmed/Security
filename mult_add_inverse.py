def gcd(num1, num2):
    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp
    if num1 == num2:
        return num2
    else:
        while num1 != 0:
            mod = num2 % num1
            num2 = num1
            num1 = mod
        return num2


def additive_inverse(m, n):
    if 0 < n < m:
        return m - n
    elif n > m:
        while n > m:
            n = n - m
        return m - n


def multiplicative_inverse(m, n):
    a1 = 1
    a2 = 0
    a3 = m
    b1 = 0
    b2 = 1
    b3 = n
    while b3 != 1:
        q = int(a3 / b3)
        t1 = a1 - q * b1
        t2 = a2 - q * b2
        t3 = a3 - q * b3
        a1 = b1
        a2 = b2
        a3 = b3
        b1 = t1
        b2 = t2
        b3 = t3
    if b2 < 0:
        while b2 < 0:
            b2 += m
        return b2
    else:
        return b2


num_1, num_2 = input().split()

num_1 = abs(int(num_1))
num_2 = abs(int(num_2))

if gcd(num_1, num_2) != 1:
    print("IMPOSSIBLE")
else:
    print(additive_inverse(num_1, num_2), multiplicative_inverse(num_1, num_2))

