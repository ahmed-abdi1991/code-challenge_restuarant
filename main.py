# main.py
from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

# Example usage:
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Tasty Burgers")
restaurant2 = Restaurant("Pizza Heaven")

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

print(customer1.restaurants())  # [restaurant1, restaurant2]
print(restaurant1.customers())  # [customer1, customer2]
print(restaurant1.average_star_rating())  # 3.5
