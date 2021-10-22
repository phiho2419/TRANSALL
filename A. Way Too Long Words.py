# '''
# A. Way Too Long Words
# https://codeforces.com/problemset/problem/71/A
# '''

num_word = int(input())

input_words = []

for word in range(num_word):
    input_words.append(input())

for i in range(len(input_words)):
    if len(input_words[i]) > 10:
        temp = input_words[i]
        input_words[i] = temp[0] + str(len(temp[1:-1])) + temp[-1]

    print(input_words[i])

