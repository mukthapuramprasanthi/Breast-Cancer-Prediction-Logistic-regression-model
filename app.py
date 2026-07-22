import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp{
    background-color:#f5f9ff;
}

.main-title {
    text-align: center;
    color: #0B5394;
    font-size: 70px;
    font-weight: bold;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: #555555;
    font-size: 20px;
    margin-bottom: 25px;
}
div.stButton > button{
    width:100%;
    height:50px;
    background:#0B5394;
    color:white;
    font-size:20px;
    border-radius:10px;
}

div.stButton > button:hover{
    background:#073763;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# ---------------- TITLE ----------------
st.markdown("""
<h1 style="
text-align:center;
color:#0B5394;
font-size:55px;
font-weight:bold;
margin-bottom:0px;">
🩺 Breast Cancer Prediction System
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style="
text-align:center;
color:#555555;
margin-top:0px;
font-size:20px;">
Enter the patient's medical measurements to predict whether the tumor is Benign or Malignant.
</h4>
""", unsafe_allow_html=True)

# ---------------- INPUT ----------------
col1, col2, col3 = st.columns(3)

with col1:
    perimeter_worst = st.number_input("Perimeter Worst", value=0.0)
    area_worst = st.number_input("Area Worst", value=0.0)
    radius_worst = st.number_input("Radius Worst", value=0.0)
    concave_points_worst = st.number_input("Concave Points Worst", value=0.0)
    concave_points_mean = st.number_input("Concave Points Mean", value=0.0)

with col2:
    perimeter_mean = st.number_input("Perimeter Mean", value=0.0)
    area_mean = st.number_input("Area Mean", value=0.0)
    radius_mean = st.number_input("Radius Mean", value=0.0)
    area_se = st.number_input("Area SE", value=0.0)
    concavity_mean = st.number_input("Concavity Mean", value=0.0)

with col3:
    concavity_worst = st.number_input("Concavity Worst", value=0.0)
    perimeter_se = st.number_input("Perimeter SE", value=0.0)
    radius_se = st.number_input("Radius SE", value=0.0)
    compactness_worst = st.number_input("Compactness Worst", value=0.0)
    compactness_mean = st.number_input("Compactness Mean", value=0.0)

st.markdown("")

if st.button("Predict"):

    input_df = pd.DataFrame([[
        perimeter_worst,
        area_worst,
        radius_worst,
        concave_points_worst,
        concave_points_mean,
        perimeter_mean,
        area_mean,
        radius_mean,
        area_se,
        concavity_mean,
        concavity_worst,
        perimeter_se,
        radius_se,
        compactness_worst,
        compactness_mean
    ]], columns=[
        "perimeter_worst",
        "area_worst",
        "radius_worst",
        "concave points_worst",
        "concave points_mean",
        "perimeter_mean",
        "area_mean",
        "radius_mean",
        "area_se",
        "concavity_mean",
        "concavity_worst",
        "perimeter_se",
        "radius_se",
        "compactness_worst",
        "compactness_mean"
    ])

    scaled_data = scaler.transform(input_df)

    prediction = model.predict(scaled_data)

    probability = model.predict_proba(scaled_data)

    st.markdown("---")

    # CHANGE THIS IF YOUR LABEL ENCODING IS REVERSED
    if prediction[0] == 1:

        confidence = probability[0][1] * 100

        st.error("## 🔴 Prediction : Malignant")

    
    else:

        

        st.success("## 🟢 Prediction : Benign")

       