import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("./disease_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit App UI
st.set_page_config(page_title="Disease Prediction", page_icon="🩺", layout="centered")

st.markdown("""
    <style>
        .stApp {background-color: #000;}
        .stButton > button {background-color: #4CAF50; color: white; font-size: 18px; border-radius: 10px;}
        .stTextInput, .stSelectbox, .stNumberInput {border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

st.title("🩺 Disease Prediction App")
st.markdown("### Enter your health details below")

# Name input
name = st.text_input("Enter Your Name")

# Layout with two columns for better UI
col1, col2 = st.columns(2, gap="medium")

with col1:
    thalach = st.number_input("**Max Heart Rate Achieved (60 - 220):**", min_value=60, max_value=220, step=1)
    exang = st.radio("**Exercise-Induced Angina**", ["No", "Yes"], horizontal=True)
    oldpeak = st.slider("**ST Depression Induced by Exercise**", min_value=0.0, max_value=6.2, step=0.1)
    cp_0 = st.radio("**Chest Pain Type 0**", ["No", "Yes"], horizontal=True)
    cp_2 = st.radio("**Chest Pain Type 2**", ["No", "Yes"], horizontal=True)

with col2:
    slope_1 = st.radio("**Slope Type 1**", ["No", "Yes"], horizontal=True)
    slope_2 = st.radio("**Slope Type 2**", ["No", "Yes"], horizontal=True)
    ca_0 = st.radio("**Major Vessels 0**", ["No", "Yes"], horizontal=True)
    thal_2 = st.radio("**Thalassemia Type 2**", ["No", "Yes"], horizontal=True)
    thal_3 = st.radio("**Thalassemia Type 3**", ["No", "Yes"], horizontal=True)

def preprocess_input():
    exang_val = 1 if exang == "Yes" else 0
    cp_0_val = 1 if cp_0 == "Yes" else 0
    cp_2_val = 1 if cp_2 == "Yes" else 0
    slope_1_val = 1 if slope_1 == "Yes" else 0
    slope_2_val = 1 if slope_2 == "Yes" else 0
    ca_0_val = 1 if ca_0 == "Yes" else 0
    thal_2_val = 1 if thal_2 == "Yes" else 0
    thal_3_val = 1 if thal_3 == "Yes" else 0
    return np.array([[thalach, exang_val, oldpeak, cp_0_val, cp_2_val, slope_1_val, slope_2_val, ca_0_val, thal_2_val, thal_3_val]])


if st.button("🔍 Predict", use_container_width=True):
    user_input = preprocess_input()
    prediction = model.predict(user_input)
    result = "not at risk of heart attack ✅" if prediction[0] == 0 else "at risk of heart attack ⚠️"
    st.markdown(f"### Your are {result}")
