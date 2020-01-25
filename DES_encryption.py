def hex2bin(hex_num, numbits):
    return bin(int(hex_num, 16))[2:].zfill(numbits)


def bin2hex(bin_num):
    return hex(int(str(bin_num), 2))


def bin2dec(bin_num):
    return int(bin_num, 2)

# -------------------------------------DES Key Generation----------------------------------------------------------#


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

    key_array = []
    for i in range(16):
        if len(array_of_keys_2[i]) < 12:
            for j in range(12):
                if len(array_of_keys_2[i]) < 12:
                    array_of_keys_2[i] = "0" + array_of_keys_2[i]
        key_array.append(array_of_keys_2[i])

    return key_array


# -------------------------------------------DES Function-----------------------------------------------------------#


def sbox(inp_in_hex):
    sbox = [

        [  # s1

            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],

            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],

            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],

            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

        ],

        [  # s2

            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],

            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],

            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],

            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

        ],

        [  # s3

            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],

            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],

            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],

            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

        ],

        [  # s4

            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],

            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],

            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],

            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

        ],

        [  # s5

            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],

            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],

            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],

            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

        ],

        [  # s6

            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],

            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],

            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],

            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

        ],

        [  # s7

            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],

            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],

            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],

            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

        ],

        [  # s8

            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],

            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],

            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],

            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],

        ]

    ]

    inp_in_bin = hex2bin(inp_in_hex, 48)
    # 1110001100101110100000111110001101100110100000
    new_inp = []
    count = 0
    for i in range(8):
        nnn = []
        for j in range(6):
            nnn.append(inp_in_bin[count])
            count += 1
        new_inp.append(nnn)

    output = ""
    for i in range(8):
        string1 = ""
        for j in range(6):
            string1 += str(new_inp[i][j])
        row = ""
        row = string1[0] + string1[5]
        row = bin2dec(row)
        column = ""
        column = string1[1] + string1[2] + string1[3] + string1[4]
        column = bin2dec(column)
        output += str(hex(sbox[i][row][column]))[2:]

    # var = str(bin2hex(output))[2 : ].upper()
    oo = output.upper()
    return "0x" + oo


def pbox(inp_in_hex):
    pbox = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

    n = 32
    inp_in_bin = hex2bin(inp_in_hex, n)
    output = ""
    for i in range(len(pbox)):
        output += inp_in_bin[pbox[i] - 1]
    hex_value = bin2hex(output)[2:]
    while len(hex_value) < 8:
        hex_value = "0" + hex_value
    return "0x" + hex_value


def epbox(inp_in_hex):
    pbox = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19,
            20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

    n = 32
    inp_in_bin = hex2bin(inp_in_hex, n)
    output = ""
    for i in range(len(pbox)):
        output += inp_in_bin[pbox[i] - 1]
    # 1010111111110110000001001100110
    return bin2hex(output)


def DES_function(new_key, new_input):
    key1 = "0x" + new_key
    out1 = epbox("0x" + new_input)
    out2 = int(out1, 0) ^ int(key1, 0)
    out3 = sbox(hex(out2))
    out4 = pbox(out3)
    return out4[2:].upper()


def inverse_initial_perm(inp_in_hex):
    pbox = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]

    n = 64
    inp_in_bin = hex2bin(inp_in_hex, n)
    output = ""
    for i in range(len(pbox)):
        output += inp_in_bin[pbox[i] - 1]

    return bin2hex(output)


def initial_perm(inp_in_hex):
    pbox = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]

    n = 64
    inp_in_bin = hex2bin(inp_in_hex, n)
    output = ""
    for i in range(len(pbox)):
        output += inp_in_bin[pbox[i] - 1]

    return bin2hex(output)

#  -------------Main------------


key = input()
plain_text = input()
N = input()
error_checking = 0
if not N.isdigit():
    error_checking = 1
else:
    N = int(N)

# -------------key generation step--------------#
keys = generate_keys(key)  # list of 16 keys



# -------------16 Rounds step---------#
index = 0
if error_checking == 0:
    for k in range(N):
        # -----------initial permutation step-----------#
        plain_text = initial_perm(plain_text)[2:]
        if len(plain_text) < 16:
            for j in range(16):
                if len(plain_text) < 16:
                    plain_text = "0" + plain_text

        left_half = plain_text[0: 8]
        right_half = plain_text[8:]
        if len(right_half) < 8 or len(left_half) < 8:
            for j in range(8):
                if len(right_half) < 8:
                    right_half = "0" + right_half
                if len(left_half) < 8:
                    left_half = "0" + left_half
        for i in range(16):
            # --------------des function step------------#
            x = DES_function(keys[i], right_half)
            y = int(left_half, 16) ^ int(x, 16)
            left_half = right_half
            right_half = hex(y)
            right_half = right_half[2:]

        if len(right_half) < 8 or len(left_half) < 8:
            for j in range(8):
                if len(right_half) < 8:
                    right_half = "0" + right_half
                if len(left_half) < 8:
                    left_half = "0" + left_half

        plain_text = right_half + left_half
        plain_text = inverse_initial_perm(plain_text)[2:].upper()
        if len(plain_text) < 16:
            for j in range(16):
                if len(plain_text) < 16:
                    plain_text = "0" + plain_text
        index = k


if error_checking == 0:
    print(plain_text)
'''
0000000000000000
FFFFFFFFFFFFFFFF
1
0000000000000000
355550B2150E2451
1
133457799BBCDFF1
0123456789abcdef
1
1111110000005555
FFFF000011119000
1
B29D9179933F7509
52BD52036FE0B133
471
'''