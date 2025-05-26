# 🧹 Automated Data Cleaning and Feature Engineering for Data Preprocessing
---
## Technologies Used
  - Python 3.x
  - Pandas, NumPy – for data manipulation
  - Scikit-learn – for feature scaling
  - Scipy – for statistical operations
  - IPython.display – for enhanced notebook visuals
---

## 📖 Overview

**AutoClean** is a Python-based automation tool that streamlines the **data cleaning and preprocessing** phase of data science and machine learning workflows. It automates everything from loading data to removing outliers — making raw data ready for analysis and modeling with minimal manual effort.

---

## 🚀 Features

### 📁 Flexible Data Loading
- Supports multiple file formats: **CSV**, **Excel (.xlsx)**, and **JSON**

### 🧪 Initial Data Quality Report
- Auto-generates insights including:
  - Number of rows and columns
  - Duplicate rows/columns
  - Missing value summary
  - Unique values per feature
  - Data types and descriptive statistics

### 🧼 Smart Data Cleaning
- Converts data types automatically
- Detects and processes:
  - Date-time columns
  - Target variable
  - Low-cardinality numeric columns (converted to categorical)
- Converts all remaining columns appropriately (e.g., string, numeric)

### 🧩 Missing Value Imputation
- Drops:
  - Columns with **>40% missing values**
  - Rows with **>40% missing values**
- Imputes missing data using:
  - **Mean/Median** (based on skewness)
  - **Mode** for categorical
  - `'xxxxx'` for strings
  - **Forward-fill** for date-time

### 📉 Outlier Removal & Feature Scaling
- Removes outliers using:
  - **IQR** method for skewed distributions
  - **Z-Score** method for normally distributed data
- Supports multiple scaling methods:
  - ⚖️ Z-Score (StandardScaler)
  - 📊 Min-Max Scaling
  - 🧱 Robust Scaling
  - ⬆️ MaxAbs Scaling

