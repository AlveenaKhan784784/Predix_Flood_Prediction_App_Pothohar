# 🌧️ Predix: Flood Prediction App

This project predicts the probability of flooding based on recent weather data such as rainfall, temperature, wind speed, and humidity. It uses NASA’s open data and a trained machine learning model to provide early flood risk alerts.

---

## 🚀 Features
- Predicts flood probability using rainfall and weather parameters  
- Simple Streamlit web interface  
- Works with real-time weather data  
- Easy to use for environmental monitoring and research  

---

## 🧠 Data Sources & How It Works

We use data from:

- **NASA GPM (Global Precipitation Measurement)**  
- **NASA POWER (Data Access Viewer)** — a powerful tool to retrieve climatology and weather parameters for any location.  
  [POWER Data Access Viewer](https://power.larc.nasa.gov/data-access-viewer/?utm_source=chatgpt.com) 

How it works:

1. Input rainfall, temperature, wind speed, and humidity data (obtained from these datasets).  
2. The trained model calculates the flood probability.  
3. The app displays whether there’s a flood alert or not.  

---

## 🛠️ Technologies Used
- **Python**  
- **Streamlit**  
- **Pandas**  
- **Scikit-learn**  
- **NumPy**  
- **NASA GPM & NASA POWER datasets**  

---
