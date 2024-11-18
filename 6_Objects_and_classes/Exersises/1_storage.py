
class Storage:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = []  # Initializes an empty list to store products

    def add_product(self, product: str):
        # Checks if there is enough space before adding the product
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        # Returns the list of products in storage
        return self.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
