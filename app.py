import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Title
st.title("💎 Diamond Price Prediction")

# Numerical Inputs
carat = st.number_input("Carat", min_value=0.0, value=0.5)
depth = st.number_input("Depth", min_value=0.0, value=61.0)
table = st.number_input("Table", min_value=0.0, value=55.0)
x = st.number_input("x", min_value=0.0, value=5.0)
y = st.number_input("y", min_value=0.0, value=5.0)
z = st.number_input("z", min_value=0.0, value=3.0)

# Categorical Inputs
cut = st.selectbox("Cut", ["Fair","Good","Very Good","Premium","Ideal"])
color = st.selectbox("Color", ["D","E","F","G","H","I","J"])
clarity = st.selectbox("Clarity", ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"])

# Prediction Button
if st.button("Predict"):
    try:
        # Create input dataframe (IMPORTANT: same order as training)
        input_df = pd.DataFrame(
            [[carat, depth, table, x, y, z, cut, color, clarity]],
            columns=["carat","depth","table","x","y","z","cut","color","clarity"]
        )

        # Predict
        prediction = model.predict(input_df)

        # Output
        st.success(f"💰 Predicted Price: ${prediction[0]:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")