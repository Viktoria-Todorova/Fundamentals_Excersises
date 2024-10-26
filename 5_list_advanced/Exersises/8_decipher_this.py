
secret_message = input().split()
decoded_word = []

for word in secret_message:
    first_letter = ""
    rest_of_word = ""
    word_final = ""

    for charachter in word:
        if charachter.isdigit():
            first_letter += charachter
        else:
            rest_of_word += charachter
    first_letter_s = chr(int(first_letter))
    word_final += first_letter_s

    if rest_of_word:
        if len(rest_of_word) > 1:
            second_letter = rest_of_word[0]
            last_letter = rest_of_word[-1]
            rest_of_text = rest_of_word[1:-1]
            word_final += last_letter + rest_of_text + second_letter
        else:
            word_final += rest_of_word

    decoded_word.append(word_final)




print(" ".join(decoded_word))
