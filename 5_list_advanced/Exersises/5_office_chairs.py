number_of_rooms = int(input())
total_free_chairs = 0
for room in range(1, number_of_rooms+1):
    chairs_info = input().split()
    number_visitor = int(chairs_info[-1])
    number_of_chairs = len(chairs_info[0])
    difference = number_of_chairs - number_visitor
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room}")
    total_free_chairs += difference

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
