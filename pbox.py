def hex2bin(hex_num, numbits):
    return bin(int(hex_num, 16))[2:].zfill(numbits)


def bin2hex(bin_num):
    return hex(int(str(bin_num), 2))


s = int(input())  # size of the output (size of pbox)
# parsing pbox
pbox = list(map(int, input().split()))
n = int(input())  # size of input
inp_in_hex = input()
inp_in_bin = hex2bin(inp_in_hex, n)


output = ""
for i in range(len(pbox)):
    output += inp_in_bin[pbox[i]-1]


var = str(bin2hex(output))[2 : ].upper()
print(var)
 