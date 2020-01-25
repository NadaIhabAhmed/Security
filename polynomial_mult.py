def str2hex(s):
    return int(s, 16)


def hex2bin(hex_num, numbits):
    return bin(int(hex_num, 16))[2:].zfill(numbits)


def add(num1, num2):
    temp = str2hex(num1) ^ str2hex(num2)
    return str(hex(temp))[2:].upper().zfill(2)


def index_one(num):
    num = str(bin(num))[2:]
    for i in  range(8):
        if len(num) < 8:
            num = '0' + num
    arr = []
    for i in range(8):
        if num[i] == "1":
            arr.append(7 - i)
    return arr


def mul(num1, num2):
    num1 = str2hex(num1)
    num2 = str2hex(num2)
    arr = index_one(num2)
    list_num = [num1]
    for i in range(7):
        if num1 & 128 == 128:  # 128 -> 0x80 (make sure that the first bit is one)
            num1 = ((num1 << 1) ^ 27) & 255
            list_num.append(num1)  # 27 -> 0x1b
        else:
            num1 = (num1 << 1) & 255
            list_num.append(num1)
    new_list = []
    for i in range(len(list_num)):
        if i in arr:
            new_list.append(list_num[i])

    out = 0
    for i in range(len(new_list)):
        out ^= new_list[i]

    return str(hex(out))[2:].upper().zfill(2)


num_1, num_2 = input().split()
print(add(num_1, num_2), mul(num_1, num_2))

# print(str(format(15135, '02x')[0 : 2]).upper())





