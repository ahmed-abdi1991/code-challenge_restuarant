# code-challenge_restuarant
## Project Structure

The project follows a modular structure, organized into separate files for each class within a `models` package. The main script for testing and running the program is `main.py`.

```plaintext
|-- main.py
|-- models/
|   |-- customer.py
|   |-- restaurant.py
|   |-- review.py
Classes
Customer
The Customer class represents individuals who can write reviews. It has methods for initializing, retrieving names, fetching all customers, listing restaurants reviewed, and adding new reviews.

Restaurant
The Restaurant class represents places that can be reviewed. It has methods for initializing, retrieving the name, fetching all restaurants, listing reviews, listing customers who reviewed, and calculating the average star rating.

Review
The Review class represents the reviews written by customers for restaurants. It has methods for initializing, retrieving the rating, fetching all reviews, and retrieving the associated customer and restaurant.

Usage Example
python
Copy code
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
Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Follow the project's coding standards and conventions.

License
This project is unlicensed