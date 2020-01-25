# import numpy as np
import math


def dot(G, V, sqrt_key):
    result = []
    for i in range(sqrt_key): #this loops through columns of the matrix
        total = 0
        for j in range(sqrt_key): #this loops through vector coordinates & rows of matrix
            total += G[i][j] * V[j]
        result.append(total)
    return result

key = int(input())
pt = ""  # plain text
error_flag = 0
key_array = []
for i in range(int(math.sqrt(key))):
    newoo = []
    for j in range(int(math.sqrt(key))):
            newoo.append(0)
    key_array.append(newoo)


string_plain_text = input()
#  error checking on negative values or non digit values
for i in string_plain_text:
    if i != " ":
        if not str.isdigit(i):
            error_flag = 1
        else:
            if int(i) < 0:
                error_flag = 1

if error_flag == 0:
    x = [int(i) for i in string_plain_text.split()]  # split spaced strings into an array of integers
    # convert the integers array into a root key by root key vector (vector of dimensions root key by root key)
    iterator = 0
    for i in range(int(math.sqrt(key))):
        for j in range(int(math.sqrt(key))):
            key_array[i][j] = x[iterator]
            iterator += 1
    for i in range(int(math.sqrt(key))):
        small_key_array = []
        for j in range(int(math.sqrt(key))):
            small_key_array

    # parse the plain text
    pt = input()

    # check if plain_text's length is even or add to append X's as mush as needed
    if int(math.sqrt(key)) % 2 == 0 and len(pt) % 2 != 0 and len(pt) > int(math.sqrt(key)):
        pt = pt + "X"
    elif int(math.sqrt(key)) % 2 == 0 and len(pt) % 2 != 0 and len(pt) < int(math.sqrt(key)):
        while len(pt) < int(math.sqrt(key)):
            pt = pt + "X"
    elif int(math.sqrt(key)) % 2 != 0 and len(pt) % 2 == 0 and len(pt) < int(math.sqrt(key)):
        while len(pt) < int(math.sqrt(key)):
            pt = pt + "X"
    elif int(math.sqrt(key)) % 2 != 0 and (len(pt) % 2 == 0 or len(pt) % 2 != 0) and len(pt) > int(math.sqrt(key)):
        while len(pt) % int(math.sqrt(key)) != 0:
            pt = pt + "X"

    # don't forget to handel the case of the key being greater than the plain text


    # chop the plain text of into small vectors
    pt_arrays = []
    pt_length_old = len(pt)
    num_turns = 0
    for i in range(pt_length_old):
        h = 0
        arr = []
        for j in range((int)(math.sqrt(key))):
            arr.append(ord(pt[j]) - 65)
            h = j
        pt = pt[h + 1:]
        pt_arrays.append(arr)
        num_turns += 1
        if len(pt) == 0:
            break

    new_array = []
    for i in range(num_turns):
        new_array.append(dot(key_array, pt_arrays[i], int(math.sqrt(key))))

    new_one = []
    for i in range(num_turns):
        for j in range((int)(math.sqrt(key))):
            new_one.append(chr((new_array[i][j] % 26) + 65))

    cipher_text = ""
    for i in range(len(new_one)):
        cipher_text += new_one[i]

    print(cipher_text)
