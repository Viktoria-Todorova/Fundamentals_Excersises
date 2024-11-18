class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity  # Private attribute
        self.remaining_capacity = capacity  # Tracks the available space
        self.items = []

    def add_item(self,item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
            self.remaining_capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        item = ', '.join(self.items)
        return f"Items: {item}.\nCapacity left: {self.remaining_capacity}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
