s = int(input())  # size of the output and the input (size of pbox)
# parsing pbox
pbox = list(map(int, input().split()))

error_checking = 0

if len(pbox) < s or len(pbox) != len(set(pbox)):
    error_checking = 1


output = []
for i in range(s):
    output.append(0)
for i in range(len(pbox)):
    output[pbox[i] - 1] = i + 1

new_output = ""
for i in range(s):
    new_output += str(output[i])
    new_output += " "

if error_checking == 0:
    print(new_output)
else:
    print("IMPOSSIBLE")


	
	
	