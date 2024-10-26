def data_type(types, inp):
    if types == "int":
        result = 2 * int(inp)
        return result
    elif types == "real":
        result = 1.5 * float(inp)
        return f"{result:.2f}"
    elif types == "string":
        return f"${inp}$"

type_of_input = input()
input_data = input()
print(data_type(type_of_input,input_data))