# KNN-Classifier-and-Regressor-

This repository contains two Machine Learning projects using the K-Nearest Neighbors (KNN) algorithm:

1. KNN Classification Project
2. KNN Regression Project

These projects demonstrate both classification and regression techniques using Python, Scikit-learn, and Streamlit.

---

# Project 1: KNN Classification

## Project Overview
This project uses the K-Nearest Neighbors Classification algorithm to classify data into different categories.

The model predicts class labels based on the nearest neighboring data points.

---

## Dataset Used
Iris Dataset

### Features
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target Classes
- Setosa
- Versicolor
- Virginica

---

## Algorithm Used
- KNeighborsClassifier

---

## Steps Performed
1. Import libraries
2. Load dataset
3. Split dataset into training and testing data
4. Train KNN Classification model
5. Predict test data
6. Evaluate model accuracy

---

## Evaluation Metrics
- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Output
The model predicts flower species based on flower measurements.

---

# Project 2: KNN Regression

## Project Overview
This project uses the K-Nearest Neighbors Regressor algorithm to predict salary based on years of experience.

The project also includes a Streamlit web application for prediction. :contentReference[oaicite:0]{index=0}

---

## Dataset Used
Salary Dataset

### Feature
- YearsExperience

### Target Variable
- Salary

---

## Problem Type
Regression

Because salary is a continuous numerical value.

---

## Algorithm Used
- KNeighborsRegressor

---

## Steps Performed
1. Import libraries
2. Load dataset
3. Split dataset into training and testing data
4. Train KNN Regressor model
5. Predict salary values
6. Build Streamlit prediction app

---

## Streamlit Application
The Streamlit app allows users to:
- Enter years of experience
- Predict employee salary using the trained KNN model

---

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## Required Libraries

```txt
streamlit
pandas
numpy
scikit-learn
pickle-mixin
