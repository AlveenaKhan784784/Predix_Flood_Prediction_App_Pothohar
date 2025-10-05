# ===============================
# 🌧️ Flood Prediction Streamlit App (Lagged Features v3)
# ===============================

import streamlit as st
import pandas as pd
import pickle
from datetime import date

# 1️⃣ Load trained model (updated)
rf = pickle.load(open('rf_flood_model_v2.pkl', 'rb'))

# 2️⃣ App title
st.title("🌧️ Flood Prediction App")
st.write("Predict flood risk using past 3 days of rainfall and current weather conditions.")

# 3️⃣ User inputs
st.subheader("Enter Weather Details")

rain1 = st.number_input("Rainfall 3 days ago (mm)", min_value=0.0, step=0.1, value=0.0)
rain2 = st.number_input("Rainfall 2 days ago (mm)", min_value=0.0, step=0.1, value=0.0)
rain3 = st.number_input("Rainfall yesterday (mm)", min_value=0.0, step=0.1, value=0.0)

temp = st.number_input("Average Temperature Today (°C)", min_value=-50.0, max_value=60.0, value=25.0)
wind = st.number_input("Wind Speed Today (m/s)", min_value=0.0, step=0.1, value=3.0)
humidity = st.number_input("Humidity Today (%)", min_value=0, max_value=100, value=70)

selected_date = st.date_input("Forecast Date", value=date.today())

# 4️⃣ Feature engineering (matches training)
precip_roll_3 = (rain1 + rain2 + rain3) / 3
humidity_roll_3 = humidity  # using today's humidity as proxy

df_input = pd.DataFrame({
    'Avg_Temp_C': [temp],
    'WindSpeed_mps': [wind],
    'Humidity_pct': [humidity],
    'Month': [pd.to_datetime(selected_date).month],
    'DayOfYear': [pd.to_datetime(selected_date).dayofyear],
    'precip_roll_3': [precip_roll_3],
    'humidity_roll_3': [humidity_roll_3]
})

# 5️⃣ Prediction block
if st.button("Predict Flood Risk"):
    flood_prob = rf.predict_proba(df_input)[:, 1][0]

    # 5–10% threshold for testing extreme rainfall
    threshold = 0.05
    flood_pred = int(flood_prob >= threshold)

    # Show message
    if flood_pred == 1:
        st.error(f"⚠️ Flood Alert! Probability: {flood_prob:.2f}")
    else:
        st.success(f"No Flood! Probability: {flood_prob:.2f}")

    # Show input + prediction table
    df_input['Flood_Prediction'] = ['Flood Alert!' if flood_pred == 1 else 'No Flood!']
    df_input['Flood_Probability'] = flood_prob
    st.subheader("Prediction Details")
    st.dataframe(df_input)

# 6️⃣ Optional: debug info for probabilities
if st.checkbox("Show probability range for testing"):
    st.write(f"Rolling precipitation: {precip_roll_3} mm")
    st.write(f"Predicted probability: {flood_prob:.2f}")
