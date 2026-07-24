


class Tv:
    def __init__(self,model,price):
        self.model = model
        self.price = price
    
    def get_price(self):
        return self.price
    
    def get_model(self):
        return self.model
    

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






amazon = Cart("Amazon",[])



model = input("model:")
price = input("price:")

brand = Tv(model,price)

amazon.items.append(brand.model)

print(amazon.shopping_cart_items())


