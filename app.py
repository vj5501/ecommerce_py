from codecarbon import OfflineEmissionsTracker

class Product:
    def __init__(self, name, id, price):
        self.name = name
        self.id = id
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added to cart")

    def remove_product(self, product):
        self.products.remove(product)

    def display_cart(self):
        if not self.products:
            print("No products Cart is empty!")
        else:
            print("Cart contains products")
            for product in self.products:
                print(f"-{product.name}"+f"  ${product.price}")

    def remove_from_cart(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Removed {product.name} from cart")

    def calculate_total(self):
        tracker=OfflineEmissionsTracker(country_iso_code='IND')
        tracker.start()
        total = 0
        for product in self.products:
            total = total+product.price
        return total
        tracker.stop()


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product):
        self.shopping_cart.add_product(product)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_from_cart(product)

    def checkout(self):
        total = self.shopping_cart.calculate_total()
        print("Total amount to pay: $", total)


# cmdline iNTERFACE
pr1 = Product("Washing Machine", 1, 80000)
pr2 = Product("Iron Machine", 2, 800)
pr3 = Product("Phaser Machine", 3, 80858)
pr4 = Product("Laser Machine", 4, 80057)


customer = Customer("Vishnu Jadhav", "VishnuJadhav5501@gmail.com")
print("Welcome to eCommerce Command Line Store")
print("here are available products  ")


products = [pr1, pr2, pr3, pr4]
for i in products:
    print(f"{i.id},{i.name} = ${i.price}")


while True:
    print("\n Select an Option")
    print("1: add product to cart")
    print("2: Display cart")
    print("3: Remove from cart")
    print("4:checkout and show total")
    user_input = input("Enter Your choice: ")

    if user_input == "1":
        print("Please Select Procuct to add to cart")
        product_id = int(input("Enter Procuct ID to add to cart"))
        selected_product = next(
            (product for product in products if product.id == product_id), None)
        if selected_product:
            customer.add_to_cart(selected_product)
        else:
            print("Invalid Product Selected")

    elif user_input == "2":
        customer.shopping_cart.display_cart()

    elif user_input == "3":
        print("Please Select Procuct to remove to cart")
        product_id = int(input("Enter Procuct ID to Remove to cart"))
        selected_product = next(
            (product for product in products if product.id == product_id), None)
        if selected_product:
            customer.remove_from_cart(selected_product)
        else:
            print("Invalid Product Selected")

    elif user_input == "4":
        customer.checkout()
        break

    else:
        print("Invalid input here, Please try again later")
