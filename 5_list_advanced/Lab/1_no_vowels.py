text = list(input())

new_text = [ letter for letter in text if letter.lower() not in "aouei"]
print("".join(new_text))