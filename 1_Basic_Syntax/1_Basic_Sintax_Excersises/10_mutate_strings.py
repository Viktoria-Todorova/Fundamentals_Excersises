string_1 = input()
string_2 = input()
word = ""
for letter in range(len(string_1)+1):

    left_side = (string_2[:letter])
    right_side = (string_1[letter:])
    current_word = left_side + right_side

    if current_word != word and current_word != string_1:
        print(current_word)
        word = current_word
0