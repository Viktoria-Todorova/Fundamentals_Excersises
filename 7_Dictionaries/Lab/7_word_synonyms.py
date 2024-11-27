count_of_words = int(input())
list_of_synonyms = {}
for synonyms in range(count_of_words):
    word = input()
    synonym = input()

    if word not in list_of_synonyms:
        list_of_synonyms[word] = []

    list_of_synonyms[word].append(synonym)
for word in list_of_synonyms:
    print(f"{word} - {', '.join(list_of_synonyms[word])}")


