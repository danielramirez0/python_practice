from customer import Customer
from product import Product

customer_one = Customer("John")
product_one = Product("Shoes", "44.99", "Clothing")
product_two = Product("T-Shirt", "14.99", "Clothing")
product_three = Product("iPhone", "999.99", "Technology")

print(f"{customer_one.name}")

customer_one.update_cart(product_one)
customer_one.update_cart(product_two)
customer_one.update_cart(product_three)

customer_one.list_products()

total = customer_one.shopping_cart.total_products()
print(f"{total}")

customer_one.shopping_cart.empty_cart()

total = customer_one.shopping_cart.total_products()
print(f"{total}")
