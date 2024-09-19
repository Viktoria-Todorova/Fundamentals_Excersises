
while True:
    final_word = ""
    word = input()

    if word == "End":
        break
    elif word != "SoftUni":
        for i in word:
            final_word += i * 2
        print(final_word)





