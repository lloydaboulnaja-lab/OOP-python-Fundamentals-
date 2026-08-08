class Cart_item:
    def __init__(self,model,):
        self.model = model
        price = self.price
    
class Cart:
    def __init__(self,store,items):
        self.store = store
        self.items = items
        items = []    
     

    def store_name(self):
        print(f"The store name is {self.store}")


    def shopping_cart_items(self):
        print(f"There are {len(self.items)} amount of items in the cart and they are; ",*self.items )

    def add_item(self):
        self.items.append()


def exit_program():
    print("Thank you for using the program!")

    exit_button = input("Press the [ENTER] button to Exit the program: ")

    print("Exiting.....")

    quit()

    


def get_details():

    while True:
        model = input("\nEnter Model:")

        
        if len(model) < 1:
            print("Please enter a valid item name!")
        elif model.isdigit():
            print("The item cannot be a number!")
        else:
            break

    Store.items.append(model)



Store = Cart("Amazon",[])



def view_cart():
    
    print(f"\n{Store.shopping_cart_items()}")




def remove_items():

     print(*Store.items)

     while True:
            item_to_remove = input("\nEnter item to remove:")
    
            if len(item_to_remove) < 1:
                print("Please enter a valid item name!")
            elif item_to_remove.isdigit():
                print("The item cannot be a number!")
            elif item_to_remove not in Store.items:
                print("Item entered is not in your shopping cart!. Try again.")
            else:
                Store.items.remove(item_to_remove)
                print(f"{item_to_remove} has succesfully been removed from your shopping cart!.")
                view_cart()
                break
    



def drink_menu():
    print("="* 30)
    print

def main():
    flag = True

    print("#"*20)
    print("\n## 1. Add Items")
    print("## 2. View Cart")
    print("## 3. Remove Items")
    print("## 4. Exit Program")
    print("")
    print("#"*20)

    while flag:
        try:
            choice = int(input("\nEnter a choice from the options above: "))
        except ValueError:
            print("Your choice Must be a number (1-4) ")
            continue

        if choice not in [1,2,3,4,5]:
            print("Invalid choice!.")

        elif choice == 1:
            get_details()

        elif choice == 2:
            view_cart()

        elif choice == 3:
            if len(Store.items) == 0:
                print("\nThere is no items in your cart to remove!.")
            else:
                remove_items()
                continue
            
        elif choice == 4:
            exit_program()

        else:
            break

    


if __name__ == "__main__":
    main()
