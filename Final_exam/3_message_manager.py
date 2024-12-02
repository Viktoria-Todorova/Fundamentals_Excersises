capacity = int(input())

messages_manager = {}

while True:
    command = input()
    if command == "Statistics":
        break
    command_to_split = command.split("=")
    action = command_to_split[0]

    if action == "Add":
        username = command_to_split[1]
        sent = int(command_to_split[2])
        received = int(command_to_split[3])
        if username not in messages_manager:
            messages_manager[username] = [sent, received]

    elif action == "Message":
        sender = command_to_split[1]
        receiver = command_to_split[2]
        if sender in messages_manager and receiver in messages_manager:
            messages_manager[sender][0] +=1
            messages_manager[receiver][0] +=1
            if messages_manager[sender][0] + messages_manager[sender][1] == capacity:
                print(f"{sender} reached the capacity!")
                del messages_manager[sender]
            if messages_manager[receiver][0] + messages_manager[receiver][1] == capacity:
                print(f"{receiver} reached the capacity!")
                del messages_manager[receiver]

    elif action == "Empty":
        username = command_to_split[1]
        if username in messages_manager:
            del messages_manager[username]
        if username =="All":
            messages_manager.clear()

print(f"Users count: {len(messages_manager)}")

for key, value in messages_manager.items():
    print(f"{key} - {value[0] + value[1]}")