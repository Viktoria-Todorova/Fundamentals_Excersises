some_text = input().split()
filter_words = (word for word in some_text if len(word) %2 == 0)
print("\n".join(filter_words))