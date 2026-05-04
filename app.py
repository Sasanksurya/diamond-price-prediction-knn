import streamlit as st
import pickle
import pandas as pd

# Load model
import joblib

model = joblib.load("model.pkl")

st.title("💎 Diamond Price Prediction")

# Inputs
carat = st.number_input("Carat")
depth = st.number_input("Depth")
table = st.number_input("Table")
x = st.number_input("x")
y = st.number_input("y")
z = st.number_input("z")

cut = st.selectbox("Cut", ["Fair","Good","Very Good","Premium","Ideal"])
color = st.selectbox("Color", ["D","E","F","G","H","I","J"])
clarity = st.selectbox("Clarity", ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"])

# Predict
if st.button("Predict"):
    input_df = pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]],
        columns=["carat","cut","color","clarity","depth","table","x","y","z"])
    
    prediction = model.predict(input_df)
    st.success(f"Predicted Price: ${prediction[0]:.2f}")