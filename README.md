# 🚗 Car Resale Price Prediction

An end-to-end Machine Learning project that predicts the resale price of used cars using regression techniques. The project includes data cleaning, feature engineering, exploratory data analysis, model comparison, hyperparameter tuning, and a Streamlit web application for real-time price prediction.

---

# 📌 Project Overview

Accurately estimating the resale value of a used car helps buyers, sellers, and dealerships make informed pricing decisions.

This project develops a regression model that predicts car resale prices based on vehicle specifications such as engine capacity, mileage, fuel type, transmission, and age.

---

# 🎯 Business Problem

Used car prices vary significantly depending on multiple factors.

The objective is to build a machine learning model that can estimate a fair resale price and identify the key features influencing vehicle value.

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

# 📂 Project Structure

```
Car-Resale-Price-Prediction/
│
├── car_resale_price_prediction.ipynb
├── app.py
├── data/
    ├──car_resale_prices.csv
├── car_resale_price_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
```

---

# 📊 Dataset

The dataset contains information about used cars, including:

- Selling Price
- Engine Capacity
- Mileage
- Fuel Type
- Transmission
- Seats
- Kilometers Driven
- Car Age
- Manufacturing Year
- Insurance
- City

---

# 🔄 Project Workflow

### 1. Data Cleaning

- Removed duplicate records
- Standardized mileage units
- Handled missing values
- Cleaned inconsistent categorical values
- Converted data into machine learning format

---

### 2. Exploratory Data Analysis

Performed detailed analysis including:

- Price Distribution
- Fuel Type Analysis
- Transmission Analysis
- Mileage Analysis
- Engine Capacity Analysis
- Year-wise Price Trends
- City-wise Listings
- Correlation Analysis

---

### 3. Feature Engineering

- Car Age
- One-Hot Encoding
- Feature Scaling
- Polynomial Features

---

### 4. Model Development

Trained and compared:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- Support Vector Regressor

---

### 5. Hyperparameter Tuning

Optimized:

- XGBoost
- Random Forest

using RandomizedSearchCV.

---

# 📈 Model Performance

Best Model: **XGBoost Regressor**

Evaluation Metrics:

- R² Score ≈ **0.87**
- RMSE ≈ **1.14**
- MAE ≈ **0.78**

---

# 🚀 Streamlit Application

The web application allows users to predict the resale price by entering:

- Engine Capacity
- Fuel Type
- Transmission
- Mileage
- Car Age
- Kilometers Driven
- Number of Seats

The model instantly returns the estimated resale price.

---

# 💡 Key Insights

- Engine capacity and vehicle age strongly influence resale value.
- Lower mileage vehicles generally command higher prices.
- Fuel type and transmission contribute significantly to price variation.
- Ensemble models outperform traditional linear regression for this dataset.

---

# 📸 Application Preview

Add screenshots of:

- Prediction interface
- Sample prediction
- Feature importance chart
- Actual vs Predicted plot

---

# 🚀 Future Improvements

- Deep Learning Regression
- SHAP Explainability
- Model Monitoring
- Vehicle Image-Based Price Prediction
- Deployment on Hugging Face or Streamlit Cloud

---

# 📚 Skills Demonstrated

### Data Analysis

- Data Cleaning
- EDA
- Feature Engineering
- Statistical Analysis

### Machine Learning

- Regression
- Model Selection
- Cross Validation
- Hyperparameter Tuning
- Ensemble Learning

### Deployment

- Streamlit
- Joblib
- Model Serialization

---

# ⭐ Repository Highlights

- End-to-End Regression Pipeline
- Real-World Dataset
- Multiple Regression Models
- Hyperparameter Optimization
- Interactive Streamlit Application
- Production-Ready Prediction Interface
