# 💎 Diamond Price Prediction (KNN)

## 📌 Overview

This project predicts diamond prices using a K-Nearest Neighbors (KNN) regression model.
It includes data preprocessing, model training, evaluation, and a Streamlit web app.

## 📂 Files

* `Diamond Price Prediction using KNN and Streamlit Deployment.ipynb` – training notebook
* `diamonds.csv` – dataset
* `model.pkl` – trained pipeline (preprocessing + model)
* `app.py` – Streamlit app
* `requirements.txt` – dependencies

## ⚙️ Model

* Algorithm: KNN Regressor
* Preprocessing: OneHotEncoding + StandardScaler (via Pipeline)
* Metrics:

  * MAE ≈ 408
  * RMSE ≈ 785
  * R² ≈ 0.96

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deployment

Deployed using Streamlit Cloud (link will be added).

## 👤 Author

Sasank Surya
