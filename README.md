# Real-Time-Prediction-Dashboard-Using-Streamlit-and-Machine-Learning
Overview of the Project
This project demonstrates a real-time prediction dashboard using Streamlit, which leverages a pre-trained Linear Regression model to predict total sales for retail products. The simulation generates data continuously, and the model provides sales predictions in real-time.

# Steps to Run the Project
1. Install Dependencies:
   Install the necessary libraries using the following command:
   pip install streamlit, pandas, scikit-learn, joblib
3. Run the Streamlit App:
   Start the Streamlit app by running:
   streamlit run app.py
This will launch the dashboard in your web browser.
4. Outputs:
   Real-time Data Table: Displays the cumulative simulated sales data.
   Line Chart: Shows the predicted sales and units sold in real-time.

# Description of the Machine Learning Model Used
1. Model: Linear Regression
   Predicts total_sales based on the features: units_sold, price_per_unit, and encoded product_type.

2. Feature Encoding:
   Uses OneHotEncoder to transform the categorical product_type feature into numerical     format for model compatibility.

3. Streamlit Dashboard:
   Data Simulation: Generates synthetic data (product types, units sold, and price per unit) continuously.
   Real-Time Predictions: The model predicts total_sales for each simulated data point.
   Visualization: Displays the cumulative data and line charts for predicted sales and units sold.

