number_of_cars = int(input())
cars_with_info_dict = {}
for cars in range(number_of_cars):
    cars_info = input().split("|")
    car = cars_info[0]
    mileage = int(cars_info[1])
    fuel = int(cars_info[2])
    cars_with_info_dict[car] = [mileage, fuel]

while True:
    command = input()
    if command == "Stop":
        break
    splited_command = command.split(" : ")
    action = splited_command[0]
    current_car = splited_command[1]

    if action == "Drive":
        distance = int(splited_command[2])
        current_fuel = int(splited_command[3])
        if current_car in cars_with_info_dict.keys():

            if current_fuel > int(cars_with_info_dict[current_car][1]):
                print("Not enough fuel to make that ride")
            else:
                cars_with_info_dict[current_car][0] += distance
                cars_with_info_dict[current_car][1] -= current_fuel
                print(f"{current_car} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")

            if cars_with_info_dict[current_car][0] >= 100000:
                print(f"Time to sell the {current_car}!")
                del cars_with_info_dict[current_car]

    elif action == "Refuel":
        fuel = int(splited_command[2])
        if current_car in cars_with_info_dict.keys():
            if fuel + int(cars_with_info_dict[current_car][1]) <= 75 :
                cars_with_info_dict[current_car][1] += fuel
                print(f"{current_car} refueled with {fuel} liters" )
            else:
                extra_fuel = 75 - int(cars_with_info_dict[current_car][1])
                cars_with_info_dict[current_car][1] = 75
                print(f"{current_car} refueled with {extra_fuel} liters")

    elif action == "Revert":
        km = int(splited_command[2])
        if current_car in cars_with_info_dict.keys():
            cars_with_info_dict[current_car][0] -= km
            print(f"{current_car} mileage decreased by {km} kilometers")
            if cars_with_info_dict[current_car][0] < 10000:
                cars_with_info_dict[current_car][0] = 10000

for cars,(mileage,fuel) in cars_with_info_dict.items():
    print(f"{cars} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")

