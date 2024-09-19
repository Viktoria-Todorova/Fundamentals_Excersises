random = input().lower()
counter = 0

list_words =["sand", "water", "fish", "sun"] # Define a list of target words

for word in list_words:
    counter += random.count(word) # Count occurrences of each target word

print(counter)

