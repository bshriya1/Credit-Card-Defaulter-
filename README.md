# 💳 Credit Card Default Prediction

An end-to-end machine learning project that predicts whether a customer is likely to default on their credit card payment based on their demographic information, credit limit, repayment history, bill amounts, and previous payment behavior — built from raw data through preprocessing, model comparison, tuning, and deployment as an interactive Streamlit app.

## 📌 Overview

Credit card companies need to identify customers who are at higher risk of defaulting so they can take appropriate preventive measures. This project uses historical customer and payment data to build a classification model that predicts whether a customer will default on their next payment.

The project compares multiple machine learning algorithms and selects the best-performing model based on classification metrics.

## 🎯 Problem Statement

Given a customer's demographic information, credit limit, repayment history, bill amounts, and previous payment amounts, predict whether the customer will default on their credit card payment.

* **0 → No Default**
* **1 → Default**

## 🗂️ Project Structure

```text
├── CreditEDA.ipynb                   # Exploratory Data Analysis
├── model_building.ipynb              # Model training & evaluation
├── app.py                            # Streamlit web application
├── Gb_model.pkl                      # Trained machine learning model
└── requirements.txt                  # Project dependencies
```

## 🔍 Workflow

1. **Data Collection** — Used a historical credit card customer dataset containing approximately 30,000 customer records.

2. **Data Cleaning** — Checked for missing values, duplicate records, inconsistent data, and irrelevant columns.

3. **EDA** — Analyzed customer demographics, credit limits, repayment status, bill amounts, payment amounts, and the distribution of default and non-default customers.

4. **Preprocessing** — Prepared numerical and categorical features for machine learning and applied feature scaling where required.

5. **Feature Selection** — Identified relevant features from customer demographic information, repayment history, billing information, and payment history.

6. **Model Building** — Trained and compared multiple classification algorithms:

   * Logistic Regression
   * K-Nearest Neighbors
   * Decision Tree
   * Random Forest
   * Support Vector Machine
   * Naive Bayes
   * Gradient Boosting

7. **Model Evaluation** — Evaluated the models using:

   * Accuracy
   * Precision
   * Recall
   * F1-Score
   * Confusion Matrix

8. **Hyperparameter Tuning** — Applied `RandomizedSearchCV` to optimize the Gradient Boosting model and identify better-performing hyperparameters.

9. **Deployment** — Built an interactive Streamlit application that allows users to enter customer information and receive a credit card default prediction.

## 🏆 Results

The dataset contains a significantly larger number of non-default cases than default cases, making it important to consider metrics beyond accuracy.

The tuned Gradient Boosting model achieved approximately:

| Metric                | Score |
| --------------------- | ----: |
| Accuracy              | ~0.82 |
| F1-Score — Default    | ~0.48 |
| Recall — Default      | ~0.36 |
| F1-Score — No Default | ~0.89 |

The model was evaluated using multiple classification metrics to understand its performance, particularly its ability to identify customers who may default.

## 🖥️ App Features

The Streamlit application allows users to provide customer information and receive a prediction.

### Input Features

* Credit Limit
* Age
* Repayment Status
* Bill Amounts
* Previous Payment Amounts
* Other relevant customer and credit information

### Output

The application provides a prediction indicating whether the customer is:

* **Likely to Default**
* **Not Likely to Default**

## ⚙️ Tech Stack

* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn
* **Visualization:** Matplotlib, Seaborn
* **Model Tuning:** RandomizedSearchCV
* **Deployment:** Streamlit
* **Model Saving:** Joblib

## 🤖 Machine Learning Models

The following classification algorithms were explored and compared:

* Logistic Regression
* K-Nearest Neighbors
* Decision Tree
* Random Forest
* Support Vector Machine
* Naive Bayes
* Gradient Boosting

Gradient Boosting was further optimized using `RandomizedSearchCV`.

## 📊 Dataset

The project uses the **UCI Credit Card Default dataset**, containing approximately 30,000 customer records.

The dataset includes information such as:

* Customer credit limit
* Age
* Repayment status
* Bill amounts
* Previous payment amounts
* Default payment status

The target variable represents whether the customer defaulted on their credit card payment.

## 🔮 Future Improvements

* Improve recall for the default class through additional class-imbalance techniques.
* Perform more extensive hyperparameter optimization.
* Add model explainability using SHAP.
* Experiment with ensemble and advanced boosting techniques.
* Improve the Streamlit interface with probability scores and visual explanations.
* Deploy the application on a cloud platform for public access.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <https://github.com/bshriya1/Credit-Card-Defaulter->
cd Credit-Card-Default-Prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```
