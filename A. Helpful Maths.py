'''
A. Helpful Maths
https://codeforces.com/problemset/problem/339/A
'''

input = input()

num_of_1 = num_of_2 = num_of_3 = 0
for idx in range(0, len(input), 2):

    if input[idx] == '1':
        num_of_1 += 1
    elif input[idx] == '2':
        num_of_2 += 1
    elif input[idx] == '3':
        num_of_3 += 1

result = ""
for idx in range(0, num_of_1):
    result += "1"

    if idx < num_of_1 - 1:
        result += "+"

    if (idx == num_of_1 - 1) and (num_of_3 != 0 or num_of_2 != 0):
        result += "+"

for idx in range(0, num_of_2):
    result += "2"

    if idx < num_of_2 - 1:
        result += "+"

    if (idx == num_of_2 - 1) and (num_of_3 != 0):
        result += "+"

for idx in range(0, num_of_3):
    result += "3"

    if idx < num_of_3 - 1:
        result += "+"

print(result)

