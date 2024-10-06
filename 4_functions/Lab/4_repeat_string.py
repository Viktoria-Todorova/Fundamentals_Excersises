text = input()
counter = int(input())

def repeat():
    repeated_text = lambda a,b: a*b
    result = repeated_text(text,counter)
    return result
print(repeat())
