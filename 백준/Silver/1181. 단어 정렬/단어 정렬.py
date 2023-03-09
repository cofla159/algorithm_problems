n = int(input())
words = {}
max = 0
for _ in range(n):
    word = input()
    length = len(word)
    if words.get(length) == None:
        words[length] = set()
    words[length].add(word)
    if length > max:
        max = length

for i in range(1, max+1):
    if words.get(i) != None:
        new_list = sorted(list(words[i]))
        for j in range(len(new_list)):
            print(new_list[j])
