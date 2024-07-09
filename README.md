# Customer Attrition Prediction in Banking

This project tackles the challenge of predicting customer attrition in a banking context. It leverages machine learning models to identify customers at risk of leaving, allowing banks to proactively implement retention strategies.

## Key Achievements

- **High-Performance Model**: A customer attrition classification model was built using Random Forest and XGBoost algorithms, achieving an accuracy of 87%. This indicates the model's strong ability to correctly classify churning and non-churning customers.

- **Balanced Approach**: Model optimization focused on achieving a balanced F1 score of 0.63. The F1 score considers both precision (predicting churn correctly) and recall (not missing churned customers), ensuring the model performs well in identifying both types of customers.

- **Interactive Web App**: A user-friendly Streamlit web application was developed. This allows users to visualize the model's behavior and potentially interact with it to explore customer churn risk factors.
  - **Link**: [Streamlit Web App](https://frontendpy-h24q76f4ncj9qnnd2u6zkp.streamlit.app/)

## Benefits

- **Reduced Churn**: By predicting potential churn, banks can implement targeted interventions to retain valuable customers, leading to increased customer lifetime value.

- **Data-Driven Decisions**: The model provides insights into customer churn, allowing banks to make data-driven decisions regarding retention strategies and resource allocation.

- **Improved Customer Experience**: Proactive retention efforts can lead to a more positive customer experience, fostering stronger bank-customer relationships.

## Project Structure

- **data/**: Contains the dataset used for model training and testing.
- **notebooks/**: Jupyter notebooks for data exploration, model building, and evaluation.
- **models/**: Saved machine learning models.
- **app/**: Streamlit web application code.
- **requirements.txt**: Python dependencies required to run the project.
- **README.md**: Project documentation.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/pkarthikeya1/Bank_Customer_Attrition_Prediction_Service.git
   
2. Navigate to the folder:
   ```sh
   cd Bank_Customer_Attrition_Prediction_Service
3. Install poetry :
   ```sh
   pip intstall poetry
4. Install requirements using poetry :
   ```sh
   poetry install
5. Run the streamlit app
   ```sh
   streamlit run src/frontend.py


