from shopping_cart import ShoppingCart
class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()
    
    def update_cart(self, product):
        self.shopping_cart.add_product(product)

    def list_products(self):
        for item in self.shopping_cart.products:
            print(f"Category: {item.category}, Name: {item.name}, Price: {item.price}")
