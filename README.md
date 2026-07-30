# Loan Approval Prediction System

A Machine Learning web application that predicts whether a loan application is likely to be approved based on applicant and financial information.

The application is built using **Logistic Regression**, **StandardScaler**, and **Streamlit**, providing real-time predictions through a simple and interactive web interface.

---

# Live Demo

**Streamlit Application**

https://loan-approval-predictor-2026.streamlit.app/

---

# GitHub Repository

https://github.com/gmafsd775/Project_2_Loan_Approval

---

# Project Overview

This project demonstrates an end-to-end Machine Learning classification workflow for predicting loan approval decisions.

Users enter applicant and financial information through a Streamlit web application. The trained Logistic Regression model processes the input and predicts whether the loan application is likely to be approved. The application also displays the prediction confidence score.

---

# Features

- Real-time loan approval prediction
- Professional Streamlit user interface
- Logistic Regression classification model
- Prediction confidence score
- Automatic feature scaling using StandardScaler
- Input validation
- Fast prediction response
- Clean and user-friendly interface

---

# Machine Learning Model

| Item | Details |
|------|---------|
| Algorithm | Logistic Regression |
| Problem Type | Binary Classification |
| Feature Scaling | StandardScaler |
| Model Serialization | Joblib |

---

# Input Features

The model uses the following applicant information:

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

# Technology Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

# Project Structure

```text
Project_2_Loan_Approval/
│
├── app.py
├── Loan_Approval_Model.pkl
├── Loan_Approval_Scaler.pkl
├── loan_approval.csv
├── requirements.txt
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/gmafsd775/Project_2_Loan_Approval
```

## Navigate to the Project Folder

```bash
cd Project_2_Loan_Approval
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

---

# Project Workflow

1. Data Collection
2. Data Cleaning
3. Data Preprocessing
4. Feature Scaling
5. Model Training
6. Model Evaluation
7. Model Serialization
8. Streamlit Integration
9. Cloud Deployment

---

# Future Improvements

- Compare multiple classification algorithms
- Improve model explainability
- Add prediction history
- Enhance mobile responsiveness
- Add interactive dashboards and visualizations

---

# Author

**Ahmed Nawaz**

---

# Instructor

**Sir Zafar Iqbal**

---

# Year

**2026**

---

This project was developed for educational and portfolio purposes to demonstrate an end-to-end Machine Learning classification workflow using Python, Scikit-learn, and Streamlit.
