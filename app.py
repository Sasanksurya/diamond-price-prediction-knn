import streamlit as st
import pandas as pd
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

# 👇 THIS IS WHERE YOU PUT IT
if st.button("Predict"):
    input_df = pd.DataFrame(
        [[carat, depth, table, x, y, z]],
        columns=["carat","depth","table","x","y","z"]
    )

    prediction = model.predict(input_df)
    st.success(f"Predicted Price: ${prediction[0]:.2f}")