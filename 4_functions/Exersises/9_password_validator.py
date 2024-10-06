def check_password(pas):
    list_with_messages = []
    if len(pas) < 6 or len(pas) >10:
        list_with_messages.append("Password must be between 6 and 10 characters")
    if not pas.isalnum():
        list_with_messages.append("Password must consist only of letters and digits")

    count_digits = 0
    for digit in pas:
        if digit.isdigit():
            count_digits += 1
    if count_digits < 2:
        list_with_messages.append("Password must have at least 2 digits")
    return list_with_messages

password = input()
message = check_password(password)
if len(message) == 0:
    print("Password is valid")
else:
    print("\n".join(check_password(password)))