def hex2bin(hex_num, numbits):
    return bin(int(hex_num, 16))[2:].zfill(numbits)


def bin2hex(bin_num):
    return hex(int(str(bin_num), 2))

# 133457799BBCDFF1
def generate_keys(key):
    pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47,
           55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    inp_in_bin = hex2bin(key, 64)

    #  PC1
    output = ""
    for i in range(56):
        output += inp_in_bin[pc1[i] - 1]

    key = str(bin2hex(output))[2:].upper()
    if len(key) < 14:
        for j in range(14):
            if len(key) < 14:
                key = "0" + key

    first_half = hex2bin(key[0 : 7], 28)

    second_half = hex2bin(key[7 : ], 28)

    # Rotation
    array_of_keys = []
    for i in range(16):
        if i == 0 or i == 1 or i == 8 or i == 15:
            first_half = first_half[1 : ] + first_half[0]
            second_half = second_half[1 : ] + second_half[0]
            array_of_keys.append (first_half + second_half)

        else:
            first_half = first_half[2 : ] + first_half[0] + first_half[1]
            second_half = second_half[2 : ] + second_half[0] + second_half[1]
            array_of_keys.append(first_half + second_half)

    # PC2
    array_of_keys_2 = []

    for i in range(16):
        new_key = array_of_keys[i]
        output = ""
        for i in range(48):
            output += new_key[pc2[i] - 1]

        key_2 = str(bin2hex(output))[2:].upper()
        array_of_keys_2.append(key_2)
    return array_of_keys_2


generate = generate_keys(input())


for i in range(16):
    if len(generate[i]) < 12:
        for j in range(12):
            if len(generate[i]) < 12:
                generate[i] = "0" + generate[i]

    print(generate[i])




