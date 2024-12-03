import streamlit as st  # Streamlit for building interactive web apps
import pandas as pd  # For handling data in tabular form
import joblib  # For loading saved models and encoders
from data_simulation import simulate_data  # Import data simulation function

# Load the pre-trained model and encoder
model = joblib.load("regression_model.pkl")
encoder = joblib.load("product_type_encoder.pkl")

# Streamlit App Title
st.title("Real-Time Prediction Dashboard")

# Placeholders for displaying the data and charts
data_placeholder = st.empty()
chart_placeholder = st.empty()

# Initialize an empty DataFrame to hold the cumulative data
cumulative_data = pd.DataFrame(columns=["timestamp", "product_type", "units_sold", "price_per_unit", "predicted_sales"])

# Continuously simulate data and make predictions
for simulated_data in simulate_data():

    # Encode the 'product_type' feature using the previously trained encoder
    product_type_encoded = encoder.transform(simulated_data[["product_type"]])
    encoded_columns = encoder.get_feature_names_out(["product_type"])
    product_type_encoded_df = pd.DataFrame(product_type_encoded, columns=encoded_columns)
    
    # Concatenate the original data with the encoded features
    simulated_data_with_encoding = pd.concat([simulated_data, product_type_encoded_df], axis=1)

    # Predict the total sales using the trained regression model
    simulated_data["predicted_sales"] = model.predict(
        simulated_data_with_encoding.drop(columns=["timestamp", "product_type"])  # Drop non-predictive columns
    )

    # Update the cumulative data
    cumulative_data = pd.concat([cumulative_data, simulated_data], ignore_index=True)

    # Display the cumulative data in a dataframe format
    data_placeholder.dataframe(cumulative_data)

    # Plot a line chart of predicted sales and units sold
    numeric_data = cumulative_data[["predicted_sales", "units_sold"]].apply(pd.to_numeric, errors="coerce")
    chart_placeholder.line_chart(data=numeric_data)
