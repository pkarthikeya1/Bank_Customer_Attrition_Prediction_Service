# Import required libraries
import streamlit as st
import joblib
import pandas as pd

from paths import MODELS_DIR

# Load the trained LightGBM model
model_path = MODELS_DIR / 'model.pkl'

with open(model_path, 'rb') as file:
    model = joblib.load(file)

# Function to predict churn
def predict_churn(input_features):
    # Predict the churn using the trained model
    prediction = model.predict(input_features)
    return prediction

# Streamlit application layout
st.title('Bank customer attrition prediction')
col = st.columns(2)

# Input fields for user to enter customer features
CreditScore = col[0].number_input('Credit Score of Customer')
Geography = col[1].selectbox('Country', ["France", "Spain", "Germany"])
Gender = col[0].selectbox('Gender', ["Female", "Male"])
Age = col[1].number_input('Enter age in years', step=1, min_value=18, max_value=150)
Tenure = col[0].number_input('Tenure of customer in years', step=1, min_value=0, max_value=100)
Balance = col[1].number_input("Enter account balance of customer")
NumOfProducts = col[0].number_input("Enter no. of products customer using", min_value=1, max_value=10)
HasCrCard = col[1].selectbox('Does customer own credit card', ["Yes", "No"])
IsActiveMember = col[0].selectbox("Is customer an active user", ["Yes", "No"])
EstimatedSalary = col[1].number_input("Estimated salary of customer")

# Convert categorical fields to numeric
Geography_num = 0 if Geography == "France" else 1 if Geography == "Spain" else 2
Gender_num = 0 if Gender == "Female" else 1
HasCrCard_num = 1 if HasCrCard == "Yes" else 0
IsActiveMember_num = 1 if IsActiveMember == "Yes" else 0

# Combine all input features into a list
input_list = [CreditScore, Age, Tenure, Balance, NumOfProducts, EstimatedSalary, Geography_num, Gender_num, HasCrCard_num, IsActiveMember_num]
input_features = [input_list]

# Convert the input list to a DataFrame
input_columns = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary', 'Geography', 'Gender', 'HasCrCard', 'IsActiveMember']
input_df = pd.DataFrame(input_features, columns=input_columns)

# Button to trigger prediction
if st.button('Predict'):
    # Call the predict_churn function with input features
    churn_prediction = predict_churn(input_df)
    st.success(f'Churn: {churn_prediction[0]}')
