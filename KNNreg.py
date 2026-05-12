import pandas as pd
import streamlit as st
import pickle

# Load trained model
with open('knn_model.pkl', 'rb') as file:
    knn_model = pickle.load(file)

# Streamlit app
st.title("Salary Prediction using KNN Regressor")

st.write("Enter Years of Experience")

# Input field
experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    step=0.1
)

# Predict button
if st.button("Predict Salary"):

    # Create DataFrame with SAME feature used during training
    input_data = pd.DataFrame(
        [[experience]],
        columns=['YearsExperience']
    )

    # Prediction
    prediction = knn_model.predict(input_data)

    # Display result
    st.success(f"Predicted Salary: ₹ {prediction[0]:.2f}")