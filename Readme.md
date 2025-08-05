# Personality Cluster Predictor

This project uses **DBSCAN clustering** to group people based on their personality traits. It includes a Flask web application that allows users to input 29 personality-related features and see which cluster they belong to.  

---

## 🚀 Features  

- 🧠 **DBSCAN-based clustering** – Detects patterns in personality data without predefined labels  
- 🌐 **Flask Web UI** – User-friendly form for predictions  
- 📊 **29 Personality Inputs** – Captures a wide range of personality traits  
- 💾 **Joblib Model Saving/Loading** – Fast and reusable trained models  
- 📈 **Metrics Tracking** – Evaluate clustering quality using standard metrics  

---

## 🛠️ Installation  

1. Clone or download the repository  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Make sure the trained model files (`scaler.joblib` and `dbscan_model.joblib`) are in the root folder.  

---

## ▶️ Usage  

1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```
3. Fill out the 29 personality trait fields and click **Predict Cluster** to see the cluster number.  

---

## 📂 Project Structure  

```
📁 personality-cluster-predictor
│── app.py
│── requirements.txt
│── README.md
│── scaler.joblib
│── dbscan_model.joblib
│── templates/
│    └── index.html
│── static/
│    └── style.css
```

---

## 📊 Model  

- **Algorithm:** DBSCAN (Density-Based Spatial Clustering of Applications with Noise)  
- **Input Features:** 29 personality-related metrics  
- **Output:** Cluster label (numeric)  

### Metrics Used:  
- **Adjusted Rand Index**  
- **Homogeneity Score**  
- **Completeness Score**  
- **V-measure**  

---

## 🔮 Future Enhancements  

- Add visual cluster plotting  
- Automatic DBSCAN parameter tuning  
- Dashboard for analytics and insights  
- Option to upload CSV for batch predictions  

---

##🖼️ App Preview

<img width="1365" height="515" alt="Screenshot 2025-08-05 141454" src="https://github.com/user-attachments/assets/c0cb3be0-b0dc-4244-908e-8a72c5b73983" />
