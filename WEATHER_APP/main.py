import pickle
import streamlit as st
import numpy as np

# Load trained model
w = pickle.load(open(r'F:\INTERSHIP\Lung Prediction\lungs.sav', 'rb'))

def predict(input_data):
    input_array = np.asarray(input_data).reshape(1, -1)
    prediction = w.predict(input_array)
    return 'Survived' if prediction[0] == 1 else 'Not Survived'

def main():
    st.title("🧬 Cancer Survival Prediction App (Manual Input)")

    # All inputs as text_input (user enters numeric values directly)
    st.markdown("⚠️ **Enter values as numbers exactly as expected (e.g., 0 or 1 for Yes/No, 0–3 for categories)**")

    age = st.text_input("Age")
    gender = st.text_input("Gender (Male=1, Female=0)")
    cancer_stage = st.text_input("Cancer Stage (Stage I=0, Stage II=1, Stage III=2, Stage IV=3)")
    family_history = st.text_input("Family History (Yes=1, No=0)")
    smoking_status = st.text_input("Smoking Status (Never=0, Former=1, Current=2, Heavy=3)")
    bmi = st.text_input("BMI")
    cholesterol_level = st.text_input("Cholesterol Level")
    hypertension = st.text_input("Hypertension (Yes=1, No=0)")
    asthma = st.text_input("Asthma (Yes=1, No=0)")
    cirrhosis = st.text_input("Cirrhosis (Yes=1, No=0)")
    other_cancer = st.text_input("Other Cancer (Yes=1, No=0)")
    treatment_type = st.text_input("Treatment Type (0–3)")
    treatment_duration = st.text_input("Treatment Duration (Days)")

    if st.button("🔍 Predict Survival"):
        try:
            input_list = [
                float(age),
                int(gender),
                int(cancer_stage),
                int(family_history),
                int(smoking_status),
                float(bmi),
                float(cholesterol_level),
                int(hypertension),
                int(asthma),
                int(cirrhosis),
                int(other_cancer),
                int(treatment_type),
                float(treatment_duration)
            ]
            result = predict(input_list)
            st.success(f"✅ Predicted Outcome: *{result}*")
        except Exception as e:
            st.error(f"❌ Error: {e}. Please ensure all inputs are numeric and properly formatted.")

if __name__ == '__main__':
    main()
