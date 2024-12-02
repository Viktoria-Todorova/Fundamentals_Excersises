
sequence_of_numbers = input().split(" ")
some_text = input()
message = []
for num_str in sequence_of_numbers:

    sum_digits_index = sum(int(digit) for digit in num_str)

    index = sum_digits_index % len(some_text)
    message.append(some_text[index])

    some_text = some_text[:index] + some_text[index + 1:]

print("".join(message))

