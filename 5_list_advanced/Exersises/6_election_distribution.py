numb = int(input())
shells = []

for num in range(1,numb+1):
    max_electrons = 2 * num ** 2

    if numb >= max_electrons:
        shells.append(max_electrons)
        numb -= max_electrons
        if numb == 0:
            break
    else:
        shells.append(numb)
        break
print(shells)
