'''
A. Watermelon
https://codeforces.com/problemset/problem/4/A
'''

w_watermelon = input()
w_watermelon = int(w_watermelon)

if w_watermelon % 2 == 0 and w_watermelon > 2:
    print('YES')
else:
    print('NO')
