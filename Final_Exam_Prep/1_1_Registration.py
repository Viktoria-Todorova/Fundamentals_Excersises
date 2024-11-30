from audioop import reverse

username = input()

while True:
    command = input()
    if command == 'Registration':
        break
    check = command.split()

    if check[0] == 'Letters':

        lower_or_upper = check[1]

        if lower_or_upper == 'Upper':
            username = username.upper()
            print(username)
        elif lower_or_upper == 'Lower':
            username = username.lower()
            print(username)

    elif check[0] == 'Reverse':
        start = int(check[1])
        end_s = int(check[2])

        if 0 <=start <= end_s <=len(username):
            reversed_str = username[start:end_s+1][::-1]
            print(reversed_str)

    elif check[0] == 'Substring':
        substring = check[1]
        if substring in username:
            result = username.replace(substring,"",1)
            print(result)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif check[0] == 'Replace':
        char = check[1]
        username = username.replace(char,"-")
        print(username)

    elif check[0] == 'IsValid':
        char = check[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")
