'''
A. Boy or Girl
https://codeforces.com/problemset/problem/236/A
'''

username = input()

count_word = 0
for idx in range(len(username)):
    for j in range(idx + 1, len(username)):
        if username[idx] == username[j]:
            count_word += 1
            break

if (len(username) - count_word) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
