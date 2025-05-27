# 📈 Building a Custom Linear Regression Class: A Comparison with Scikit-Learn

---

## 🎯 Objective

This project demonstrates the implementation of a **Linear Regression** model using two approaches:

1. **Scikit-Learn's built-in Linear Regression class**
2. A **custom-built Linear Regression class** using the **Ordinary Least Squares (OLS)** method

By comparing outputs such as coefficients and R² scores, this project aims to reinforce core concepts behind the Linear Regression algorithm and showcase how machine learning models can be implemented from scratch.

---

## 📚 What is Linear Regression?

**Linear Regression** is a supervised learning algorithm used for predicting a continuous dependent variable based on one or more independent variables. The model aims to find the best-fitting straight line (`y = b0 + b1*x1 + b2*x2 + ... + bn*xn`) that minimizes the error between predicted and actual values.

---

## 🧰 Libraries Used

- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib` *(optional for future visualization)*

---

## 🧪 Dataset

- **Dataset**: `load_diabetes()` from Scikit-Learn
- **Features**: Age, BMI, blood pressure, and other medical attributes
- **Target**: A quantitative measure of disease progression

---

## 🛠️ Implementation Steps

### ✅ Using Scikit-Learn

- Load and preprocess the dataset
- Train-test split
- Fit the `LinearRegression` model
- Predict and evaluate using R² Score

### 🧠 Custom Class: `Regression`

- Implemented using **Ordinary Least Squares (OLS)**:
  
  $$ \beta = (X^T X)^{-1} X^T y $$

- Includes:
  - `train()` – fits the model
  - `prediction()` – predicts values
  - `accuracy()` – computes R² score

---
### 🎯 Accuracy results: 

- R² Score from Scikit-Learn:  0.51 (example)
- R² Score from Custom Model:  0.51 (matching!)
