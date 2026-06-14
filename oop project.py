class Car:
    def __init__(self,company,model,price):
        self.company = company
        self.model = model
        self.price = price
       
       
   
    def get_company(self):
        return self.company
       
       
    def get_model(self):
        print(f"\nThe current available cars for {self.company} are {self.model}")
       
    def get_price(self):
        print(f"The price of {self.model} is £{self.price:.2f}")
       
    def change_price(self,price):
        self.price = price
        print(f"The price of {self.model} has been changed to £{self.price:.2f}")
            
       
class Vendor:
    def __init__(self,name,place):
        self.name = name
        self.place = place
        self.vendors = []
       
        
    def add_vendor(self):
        self.vendors.append(self.name)
        print(f'Available vendors are {self.vendors}')

def main():
   
    print("="*20)
    print('== Toyota')
    print('== Mercedes')
    print("="*20)
   
    while True:
        try:
            main_choice = int(input("\nEnter a choice from the options above: "))
        except ValueError:
            print("Invaid choice!. Please try again.")
            continue
        if main_choice == 1:
            toyota.get_model()
        elif main_choice == 2:
            benz.get_model()
        else:
           dartford_cars.add_vendor()
           
       
           
       
       
toyota = Car("Toyota","camry",10000)
benz = Car("Mercedes","SUV",23000)

dartford_cars = Vendor("Dartford cars","Dartford")
    
       

if __name__ == "__main__":
    main()

