
class Cart_item:
    def __init__(self,model,price):
        self.model = model
        self.price = price
    
    def get_price(self):
        return self.price
    
    def get_model(self):
        return self.model
    
