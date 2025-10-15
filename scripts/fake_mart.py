# Import the pandas library and give it the alias 'pd'
# Used for working with data structures like DataFrames

import pandas as pd

# Import the Faker library, which allows generating fake but realistic data, I previously installed it on cmd with pip install faker command.
from faker import Faker # type: ignore

# Import Python's built-in 'random' module for generating random numbers
import random

# Create a Faker object instance, which we’ll use to generate fake data
fake = Faker()

# Create an empty list to store each fake record (each order)
data = []

# Loop 1000 times to generate 1000 fake sales records
for _ in range(1000):
    # Append a dictionary (representing one order) to the 'data' list
    data.append(
        {   # Generate a random unique identifier for the order (UUID)
            "OrderID": fake.uuid4(),

            # Generate a random customer ID between 1000 and 9999
            "CustomerID": fake.random_int(min=1000, max=9999),

             # Generate a random word to represent a product name
            "Product": fake.word(),

            # Randomly choose one of the provided product categories
            "Category": random.choice(["Electronics", "Fashion", "Home", "Toys"]),

            # Generate a random quantity of items purchased between 1 and 10
            "Quantity": random.randint(1, 10),

            # Generate a random price between 5 and 500, rounded to 2 decimal places
            "Price": round(random.uniform(5, 500), 2),

             # Generate a random order date within the last year
            "OrderDate": fake.date_between(start_date="-1y", end_date="today")
        }
    )

    # Convert the list of dictionaries ('data') into a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file located in the 'data' folder
    # 'index=False' prevents pandas from writing row numbers as a separate column
    df.to_csv(r'C:/Users/marti/ecommerce-sales-analysis/data/data.csv', index=False)