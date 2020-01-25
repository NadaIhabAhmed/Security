key_parse = input()  # key string
pt_parse = input()  # plaintext

# initializing 5*5 vector for holding key values
error_checking = 0

for i in range(len(pt_parse)):
    if not (pt_parse[i].isalpha() or pt_parse[i].isdigit()):
        error_checking = 1
for i in range(len(key_parse)):
    if not (key_parse[i].isalpha() or key_parse[i].isdigit()):
        error_checking = 1

# remove the numbers
pt = ''.join(i for i in pt_parse if not i.isdigit())
key = ''.join(i for i in key_parse if not i.isdigit())

new_key = ""
for i in range(len(key)):
    if key[i] == "J":
        new_key += "I"
    else:
        new_key += key[i]
key = new_key

new_key = key
key = ''.join(sorted(set(new_key), key=new_key.index))

new_key = ""
for i in range(len(key)):
    if key[i] == "J":
        new_key += "I"
    else:
        new_key += key[i]
key = new_key

mat = []
for i in range(5):
    mat_new = []
    for j in range(5):
        mat_new.append(0)
    mat.append(mat_new)

# stuffing key in mat vector
if len(key) > 0 and len(pt) > 0 and error_checking == 0:
    count = 0
    if len(key) <= 5:
        for i in range(len(key)):
            mat[0][i] = key[i]
    elif len(key) > 5:
        for i in range(5):
            for j in range(5):
                if count < len(key):
                    mat[i][j] = key[count]
                    count += 1
                else:
                    break

    # Array of alphabets that will be stuffed in the remaining locations of mat

    alpha_array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                   "V", "W", "X", "Y", "Z"]  # i removed the J as it's considered as I

    # remove redundant letters

    store_index_to_be_removed = []
    for i in range(len(alpha_array)):
        for j in range(len(key)):
            if key[j] == alpha_array[i]:
                # alpha_array.remove(alpha_array[i])
                store_index_to_be_removed.append(key[j])

    for i in range(len(store_index_to_be_removed)):
        alpha_array.remove(store_index_to_be_removed[i])

    # stuffing the remaining letters of alpha_array in mat

    count = 0
    for i in range(5):
        for j in range(5):
            if (mat[i][j] == 0):
                mat[i][j] = alpha_array[count]
                count += 1

    # divide plaintext into pairs if there is a pair of matching chars insert "X" if the matching chars are "X"s, insert "Q"

    list_of_pt_chars = []  # as modifying the string didn't work
    for i in range(len(pt)):
        list_of_pt_chars.append(pt[i])

    countx = 0
    while countx < len(list_of_pt_chars) - 1:
        if countx % 2 == 0:
            if list_of_pt_chars[countx] == list_of_pt_chars[countx + 1] or list_of_pt_chars[countx] == "J" and \
                    list_of_pt_chars[countx + 1] == "I" or list_of_pt_chars[countx] == "I" and list_of_pt_chars[
                countx + 1] == "J":
                if list_of_pt_chars[countx] == "X":
                    list_of_pt_chars.insert(countx + 1, "Q")
                else:
                    list_of_pt_chars.insert(countx + 1, "X")
        countx += 2
    #  append an extra x or q if the length of the plaintext is odd
    if len(list_of_pt_chars) % 2 != 0:  # not even number
        if list_of_pt_chars[len(list_of_pt_chars) - 1] == "X":
            list_of_pt_chars.append("Q")
        else:
            list_of_pt_chars.append("X")

    #  Encrypting :"D

    count = 0
    ct = ""
    while count < len(list_of_pt_chars):
        found_1 = []
        found_2 = []
        for i in range(5):
            for j in range(5):
                #  check this if again
                if list_of_pt_chars[count] == "J" and mat[i][j] == "I":
                    found_1.append(i)
                    found_1.append(j)
                elif list_of_pt_chars[count] == mat[i][j]:
                    found_1.append(i)
                    found_1.append(j)
                #  make this if an else to speed up the code
                if list_of_pt_chars[count + 1] == "J" and mat[i][j] == "I":
                    found_2.append(i)
                    found_2.append(j)
                elif list_of_pt_chars[count + 1] == mat[i][j]:
                    found_2.append(i)
                    found_2.append(j)
        count += 2
        if (found_1[0] != found_2[0]) and (found_1[1] != found_2[1]):
            ct += mat[found_1[0]][found_2[1]]
            ct += mat[found_2[0]][found_1[1]]
        elif (found_1[1] == found_2[1]) and (found_1[0] != found_2[0]):
            ct += mat[(found_1[0] + 1) % 5][found_1[1]]
            ct += mat[(found_2[0] + 1) % 5][found_2[1]]
        elif found_1[0] == found_2[0]:
            ct += mat[found_1[0]][(found_1[1] + 1) % 5]
            ct += mat[found_2[0]][(found_2[1] + 1) % 5]

    print(ct)