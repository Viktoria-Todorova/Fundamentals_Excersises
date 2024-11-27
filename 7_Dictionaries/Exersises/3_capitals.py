country_name = input().split(", ")
capitals_name = input().split(", ")

country_capital = dict(zip(country_name, capitals_name))

for key, value in country_capital.items():
    print(f"{key} -> {value}")