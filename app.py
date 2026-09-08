import streamlit as st
import pandas as pd
import pickle


# LOAD MODEL 

with open("Gb_model.pkl", "rb") as file:
    model = pickle.load(file)


# TITLE

st.title("Credit Card Default Prediction 💳")

st.divider()

# CATEGORICAL INPUTS 

st.subheader("Customer Details 👤")

SEX = st.selectbox(
    "SEX",
    ["F", "M"]
)

EDUCATION = st.selectbox(
    "EDUCATION",
    [
        "University",
        "Graduate school",
        "High School",
        "Unknown",
        "Others",
        "0"
    ]
)

MARRIAGE = st.selectbox(
    "MARRIAGE",
    [
        "Married",
        "Single",
        "Other",
        "0"
    ]
)


#  NUMERICAL INPUTS

LIMIT_BAL = st.number_input("LIMIT_BAL", value=200000)
AGE = st.number_input("AGE", value=30)

st.divider()

st.subheader("Repayment History 📊")

st.info(
    "Repayment Status: -2 = No credit used, -1 = Paid duly, "
    "0 = Revolving credit, 1 = 1 month delay, 2 = 2 months delay, "
)

PAY_0 = st.number_input("Most Recent Repayment Status", value=0)
PAY_2 = st.number_input("Previous Repayment Status", value=0)
PAY_3 = st.number_input("2 months ago repayment status", value=0)
PAY_4 = st.number_input("3 months ago repayment status", value=0)
PAY_5 = st.number_input("4 months ago repayment status", value=0)
PAY_6 = st.number_input("5 months ago repayment status", value=0)


st.subheader("Bill Amount History 💰")
BILL_AMT1 = st.number_input("Current month bill amount", value=0)
BILL_AMT2 = st.number_input("Previous month Bill amount", value=0)
BILL_AMT3 = st.number_input("2 months ago Bill amount", value=0)
BILL_AMT4 = st.number_input("3 months ago Bill amount", value=0)
BILL_AMT5 = st.number_input("4 months ago Bill amount", value=0)
BILL_AMT6 = st.number_input("5 months ago Bill amount", value=0)


st.subheader("Payment Amount History 💵 ")
PAY_AMT1 = st.number_input("Current month payment amount", value=0)
PAY_AMT2 = st.number_input("Previous month payment amount", value=0)
PAY_AMT3 = st.number_input("2 months ago payment amount", value=0)
PAY_AMT4 = st.number_input("3 months ago payment amount", value=0)
PAY_AMT5 = st.number_input("4 months ago payment amount", value=0)
PAY_AMT6 = st.number_input("5 months ago payment amount", value=0)


# ---------------- CREATE INPUT DATAFRAME ----------------

input_data = pd.DataFrame({
    "LIMIT_BAL": [LIMIT_BAL],
    "SEX": [SEX],
    "EDUCATION": [EDUCATION],
    "MARRIAGE": [MARRIAGE],
    "AGE": [AGE],
    "PAY_0": [PAY_0],
    "PAY_2": [PAY_2],
    "PAY_3": [PAY_3],
    "PAY_4": [PAY_4],
    "PAY_5": [PAY_5],
    "PAY_6": [PAY_6],
    "BILL_AMT1": [BILL_AMT1],
    "BILL_AMT2": [BILL_AMT2],
    "BILL_AMT3": [BILL_AMT3],
    "BILL_AMT4": [BILL_AMT4],
    "BILL_AMT5": [BILL_AMT5],
    "BILL_AMT6": [BILL_AMT6],
    "PAY_AMT1": [PAY_AMT1],
    "PAY_AMT2": [PAY_AMT2],
    "PAY_AMT3": [PAY_AMT3],
    "PAY_AMT4": [PAY_AMT4],
    "PAY_AMT5": [PAY_AMT5],
    "PAY_AMT6": [PAY_AMT6]
})



if st.button("Predict Default"):
    prediction = model.predict(input_data)
    if prediction[0] in [1, "Y", "Yes"]:
        st.error("⚠️ High Risk: The customer is predicted to DEFAULT on payment.")
    else:
        st.success("✅ Low Risk: The customer is predicted NOT to default.")
