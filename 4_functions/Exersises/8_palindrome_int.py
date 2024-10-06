
def is_palindrome(num:str) -> bool:
        return num == num[::-1]

random_numbers = input().split(", ")
for current in random_numbers:
    print(is_palindrome(current))
