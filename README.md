# 🥛 Paal.AI - Milk Quality Checker  
**An IoT-enabled, Machine Learning–Powered System for Real-Time Milk Quality Monitoring**

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![IoT](https://img.shields.io/badge/IoT-Enabled-blue)
![Machine Learning](https://img.shields.io/badge/ML-LightGBM-orange)
![Firebase](https://img.shields.io/badge/Cloud-Firebase-yellow)

The **Milk Quality Checker** integrates sensor hardware, embedded programming, and machine learning to evaluate milk quality in real time.  
Designed for rural dairy farms, it brings automation, transparency, and smart analytics to traditional milk testing processes.

---

## 📌 Overview

This smart IoT platform uses **pH**, **temperature**, **density (via HX711)**, and **color (RGB)** sensors to monitor milk quality.  
A **LightGBM ML model** performs adulteration detection directly on the device, while sensor readings are stored in **Google Firebase** for cloud-level analytics.

The system is enclosed in a **3D-printed PLA housing**, providing durability and portability in dairy environments.

---

## ✨ Features

- 📡 **Real-Time Monitoring**
  - pH  
  - Temperature  
  - Density (HX711 load cell)  
  - Color (RGB)

- 🤖 **On-Device Machine Learning**
  - LightGBM model for milk adulteration detection

- ☁️ **Cloud Integration**
  - Connects to Google Firebase for live data sync

- 🧩 **3D-Printed (PLA) Enclosure**
  - Ensures durability and long-term field use

- 🐄 **Rural-Friendly & Simple Interface**
  - Designed for easy use in dairy farms

---

## 📁 Project Structure

```text
Milk-Quality-Checker/
│
├── model_training.ipynb            # ML model development and evaluation
├── generate_synthetic_data.ipynb   # Synthetic data generation
├── milk_quality.ipynb              # ML workflows for adulteration prediction
│
├── app.py                          # Device-to-cloud integration & model inference
├── firebase.js                     # Firebase web/server SDK integration
├── firebase_credentials.json       # Firebase service account file
│
└── Test_Predicted_Output.csv       # Sample prediction dataset

```

---

## 🛠️ Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/bm-bharath/Paal.AI-The-Milk-Quality-Checker
cd Paal.AI-The-Milk-Quality-Checker
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Firebase
Place your Firebase service credentials file in the project root:

```
firebase_credentials.json
```

Make sure your Firebase project includes:
- Realtime Database or Firestore  
- Proper security rules  
- Cloud Storage (optional)

---

## ▶️ Usage

### 🔧 Train Machine Learning Models
Open and run these notebooks:

- `model_training.ipynb`
- `generate_synthetic_data.ipynb`
- `milk_quality.ipynb`

### 🚀 Run IoT + ML System
```bash
python app.py
```

The system will:
- Read all sensors  
- Run LightGBM prediction  
- Upload data to Firebase  
- Save inference outputs as CSV (optional)

### 📊 View Results
- Check `Test_Predicted_Output.csv`
- Or monitor the Firebase dashboard

---

