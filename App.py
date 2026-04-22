import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("best_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🎓 Student Pass Prediction App")

st.write("Enter student details:")

# Input fields
hours = st.number_input("Hours Studied", min_value=0.0)
attendance = st.number_input("Attendance (%)", min_value=0.0)
assignments = st.number_input("Assignments Score (out of 10)", min_value=0.0)
midterm = st.number_input("Midterm Marks", min_value=0.0)
final = st.number_input("Final Marks", min_value=0.0)

if st.button("Predict"):

    input_data = np.array([[hours, attendance, assignments, midterm, final]])
    
    # Scale input
    input_data = scaler.transform(input_data)
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Student will PASS")
    else:
        st.error("❌ Student will FAIL")