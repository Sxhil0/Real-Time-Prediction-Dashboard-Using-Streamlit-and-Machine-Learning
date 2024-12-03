from sklearn.linear_model import LinearRegression  # Import Linear Regression model
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.preprocessing import OneHotEncoder  # To encode categorical features
import pandas as pd  # For handling data in tabular format
import random  # For generating random data
import joblib  # To save the trained model and encoder

# Function to train a regression model and save it along with the encoder
def train_and_save_model():
    # Define product categories
    product_types = ["Electronics", "Clothing", "Groceries", "Furniture", "Books"]

    # Generate synthetic dataset with 100 samples
    data = pd.DataFrame({
        "product_type": random.choices(product_types, k=100),  # Randomly assign product types
        "units_sold": random.choices(range(1, 10), k=100),  # Random units sold (1-9)
        "price_per_unit": [random.uniform(10, 100) for _ in range(100)]  # Random price (10-100)
    })
    # Calculate total sales for each sample
    data["total_sales"] = data["units_sold"] * data["price_per_unit"]

    # Encode the categorical 'product_type' feature
    encoder = OneHotEncoder(sparse_output=False)
    product_type_encoded = encoder.fit_transform(data[["product_type"]])

    # Create a DataFrame from the encoded features
    encoded_columns = encoder.get_feature_names_out(["product_type"])
    product_type_encoded_df = pd.DataFrame(product_type_encoded, columns=encoded_columns)

    # Combine the original data with the encoded features
    data = pd.concat([data.drop(columns=["product_type"]), product_type_encoded_df], axis=1)

    # Split the data into features (X) and target variable (y)
    X = data.drop(columns=["total_sales"])
    y = data["total_sales"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the trained model and encoder to disk
    joblib.dump(model, "regression_model.pkl")
    joblib.dump(encoder, "product_type_encoder.pkl")
    print("Model and encoder saved successfully!")

# Call the function to execute training and saving
train_and_save_model()
