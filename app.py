import streamlit as st
import joblib

st.set_page_config(
    page_title="Loan Approval Predictor",
    layout="centered"
)

# CSS Styling

st.markdown("""
<style>
div.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #1D4ED8;
}
</style>
""", unsafe_allow_html=True)

st.title("🏦Loan Approval Prediction System")
st.write("Predict whether a loan application is likely to be approved using a trained Logistic Regression model.")

## 📌 Project Overview

st.markdown("""
This project predicts whether a loan application will be approved or not using a Logistic Regression model. Users can enter applicant and financial information through a professional Streamlit web application and receive an instant prediction with model confidence.
""")

st.markdown("""
### ##  Features

- Professional Streamlit User Interface
- Logistic Regression Machine Learning Model
- Real-time Loan Approval Prediction
- Model Confidence Display
- Input Validation
- Feature Scaling using StandardScaler
- Responsive and User-Friendly Design
""")

model = joblib.load("Loan_Approval_Model.pkl")
scaler = joblib.load("Loan_Approval_Scaler.pkl")

# User Personal Information Section.

st.subheader("Personal Information")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

married = st.selectbox(
    "Married",
    ["Yes", "No"]
)
dependents = st.selectbox(
    "Dependents",
    [0, 1, 2, 3]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

st.subheader("Financial Information")

applicant_income = st.number_input(
    "Applicant Monthly Income (PKR)",
    min_value=0,
    help="Example: 50000"
)

coapplicant_income = st.number_input(
    "Co-applicant Monthly Income (PKR)",
    min_value=0,
    help="Enter 0 if there is no co-applicant."
)

loan_amount = st.number_input(
    "Requested Loan Amount (Thousands)",
    min_value=0,
    help="Example: 150"
)

loan_term = st.number_input(
    "Loan Repayment Period (Months)",
    min_value=0,
    help="Example: 360 Months (30 Years)"
)

credit_history = st.selectbox(
    "Credit History",
    ["Good", "Poor"],
    help="Good = Previous loans were paid on time."
)

property_area = st.selectbox(
    "Residential Area",
    ["Rural", "Semiurban", "Urban"]
)

#Now we start Mapping Here.

gender = 1 if gender == "Male" else 0

married = 1 if married == "Yes" else 0

education = 1 if education == "Graduate" else 0

self_employed = 1 if self_employed == "Yes" else 0

credit_history = 1 if credit_history == "Good" else 0

if st.button("Check Loan Eligibility"):

    # Basic input validation
    if applicant_income == 0:
        st.warning("Applicant income must be greater than 0.")

    elif loan_amount == 0:
        st.warning("Loan amount must be greater than 0.")

    elif loan_term == 0:
        st.warning("Loan repayment period must be greater than 0.")

    else:
        if property_area == "Rural":
            property_semiurban = 0
            property_urban = 0
        elif property_area == "Semiurban":
            property_semiurban = 1
            property_urban = 0
        else:
            property_semiurban = 0
            property_urban = 1

        input_data = [[
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            credit_history,
            property_semiurban,
            property_urban
        ]]

        # Scale the input data
        input_data = scaler.transform(input_data)

        prediction = model.predict(input_data)

        probability = model.predict_proba(input_data)
        approval_probability = probability[0][1] * 100

        if prediction[0] == 1:
            st.success("✅ Loan Approved")
            st.info(f"Model Confidence: {approval_probability:.2f}%")
        else:
            st.error("❌ Loan Not Approved")
            st.info(f"Model Confidence: {(100 - approval_probability):.2f}%")

st.sidebar.title("Project Information")

st.sidebar.markdown("### Developer")
st.sidebar.write("Ahmed Nawaz")

st.sidebar.markdown("### Machine Learning Model")
st.sidebar.write("Logistic Regression")

st.sidebar.markdown("### Instructor")
st.sidebar.write("Sir Zafar Iqbal")        

st.sidebar.markdown("### Version")
st.sidebar.write("1.0")

st.sidebar.markdown("### Year")
st.sidebar.write("2026") 

st.sidebar.markdown("### Dataset")
st.sidebar.write("Loan Approval Dataset")

# End of app