class Cart:
    def __init__(self,store,items):
        self.store = store
        self.items = items
        items = []    
     

    def store_name(self):
        print(f"The store name is {self.store}")

    def shopping_cart_items(self):
        print(f"There are {len(self.items)} amount of items in the cart and they are; {self.items}")

    def add_item(self):
        self.items.append()
