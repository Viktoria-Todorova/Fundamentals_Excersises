current_list = input()
elements = current_list.lower().split()

words_count = {}
for word in elements:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
odd_list = []
for word in words_count:
    if words_count[word] % 2 != 0:
        odd_list.append(word)
print(" ".join(odd_list))

