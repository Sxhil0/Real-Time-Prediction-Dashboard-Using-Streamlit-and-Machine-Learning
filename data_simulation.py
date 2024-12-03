import random  # For generating random values
import time  # To create delays between data generations
import pandas as pd  # To handle data in tabular form
from datetime import datetime  # To include timestamps in the data

# Function to simulate real-time data generation
def simulate_data():
    # Define a list of product types
    product_types = ["Electronics", "Clothing", "Groceries", "Furniture", "Books"]

    # Infinite loop to continuously generate data
    while True:
        # Create a dictionary representing a single row of data
        data = {
            "timestamp": [datetime.now()],  # Current timestamp
            "product_type": [random.choice(product_types)],  # Randomly pick a product type
            "units_sold": [random.randint(1, 10)],  # Random number of units sold (1-10)
            "price_per_unit": [round(random.uniform(10, 100), 2)],  # Random price per unit (10.00-100.00)
        }

        # Yield the data as a pandas DataFrame
        yield pd.DataFrame(data)

        # Pause for 5 seconds before generating the next row of data
        time.sleep(5)
