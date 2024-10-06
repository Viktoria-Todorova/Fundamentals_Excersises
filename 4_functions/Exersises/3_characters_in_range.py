
def char_range(c1, c2):
    result = []
    for ch in range(ord(c1) + 1, ord(c2)):
        result.append(chr(ch))
    return result

char_1 = input()
char_2 = input()
print(" ".join(char_range(char_1, char_2)))
