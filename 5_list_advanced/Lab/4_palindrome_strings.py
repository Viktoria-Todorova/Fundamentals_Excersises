words = input().split()
palindrome = input()
found_palindromes = []
count_palindrome = 0

for word in words:

    if word ==word [::-1]:
        found_palindromes.append(word)
    if word == palindrome:
        count_palindrome += 1
print(found_palindromes)
print(f"Found palindrome {count_palindrome} times")