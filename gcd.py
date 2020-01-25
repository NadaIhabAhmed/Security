def gcd(num1, num2):
    while num1 != 0:
        mod = num2 % num1
        num2 = num1
        num1 = mod
    return num2


num_1, num_2 = input().split()
num_1 = int(num_1)
num_2 = int(num_2)

if num_1 > num_2:
    print(gcd(num_2, num_1))
elif num_2 > num_1:
    print(gcd(num_1, num_2))
elif num_1 == num_2:
    print(num_1)
