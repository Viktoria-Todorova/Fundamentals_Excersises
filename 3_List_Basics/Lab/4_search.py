n = int(input())
word = input()
first_list = []
second_list = []
for i in range(n):
    text = input()
    first_list.append(text)

    if word in text:
        second_list.append(text)


print(first_list)
print(second_list)