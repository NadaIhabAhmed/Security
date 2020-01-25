s = list(map(int, input().split()))  # size of the output and the input (size of pbox)
size_input = int(s[0])
size_output = int(s[1])
# parsing pbox
pbox = list(map(int, input().split()))

error_checking = 0

if len(pbox) < size_input:
    error_checking = 1

output = []
for i in range(size_input):
    output.append(0)
for i in range(len(pbox)):
    if output[pbox[i] - 1] == 0:
        output[pbox[i] - 1] = i + 1
if 0 in output:
    error_checking = 1
new_output = ""
for i in range(size_input):
    new_output += str(output[i])
    new_output += " "

if error_checking == 0:
    print(new_output)
else:
    print("IMPOSSIBLE")


'''
test case
5 10
2 2 3 4 5 1 1 3 4 5
6 1 3 4 5
test case
1 2
1 1
1
test case
3 6
2 1 2 2 2 1
IMPOSSIBLE
test case
2 8
2 2 2 2 1 2 2 2 2
5 1 
test case
2 4
2 1 2 1
2 1 
test case
3 3
1 2 2
IMPOSSIBLE
'''

