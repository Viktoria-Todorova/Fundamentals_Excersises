words = input().split()

while True:
    command = input()
    if command == "Stop":
        break

    c_command = command.split()
    current_command= c_command[0]

    if current_command == "Delete":
        index = int(c_command[1])
        if 0 <= index < len(words)-1:
            words.pop(index+1)

    elif current_command == "Swap":
        word1 = c_command[1]
        word2 = c_command[2]
        if word1 in words and word2 in words:
            index1 = words.index(word1)
            index2 = words.index(word2)
            words[index1], words[index2] = words[index2], words[index1]

    elif current_command == "Put":
        word = c_command[1]
        index = int(c_command[2])
        if 0 < index < len(words):
            words.insert(index - 1 , word)
        elif index == len(words):
            words.append(word)

    elif current_command == "Sort":
        words.sort(reverse=True)

    elif current_command == "Replace":
        word1 = c_command[1]
        word2 = c_command[2]
        if word2 in words:
            index = words.index(word2)
            words[index] = word1

print(" ".join(words))


