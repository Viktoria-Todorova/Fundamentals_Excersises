class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self,sender, receiver, content, is_sent):
        info = f"{sender} says to {receiver}: {content}. Sent: {is_sent}"
        return info

emails = []
while True:
    command = input()
    if command == "Stop":
        break
    current_command = command.split(" ")
    sender = current_command[0]
    receiver = current_command[1]
    content = current_command[2]
    email = Email(sender, receiver, content)
    emails.append(email)


indices = input().split(", ")
for index in indices:
    emails[int(index)].send()
for email in emails:
    print(email.get_info(email.sender, email.receiver, email.content, email.is_sent))

