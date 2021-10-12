class ShoppingCart:
    def __init__(self):
        self.products = []

    def total_products(self):
        return len(self.products)

    def add_product(self, product):
        self.products.append(product)

    def empty_cart(self):
        self.products = []