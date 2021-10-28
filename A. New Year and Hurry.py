'''
A. New Year and Hurry
https://codeforces.com/problemset/problem/750/A
'''
input = input()

input_arr = [int(x) for x in input.split()]

no_problem = input_arr[0]
time_go_home = input_arr[1]

time_left = 4 * 60 - time_go_home

sum = 0
result = 0
for i_prob in range(0, no_problem):

    sum += (i_prob + 1) * 5
    if sum > time_left:
        break

    result += 1

print(result)

