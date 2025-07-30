 AI-Powered River Pollution Source Identifier

It is an AI-powered environmental monitoring system designed to detect, trace, and analyze pollution sources in river ecosystems using real-time data, Graph Neural Networks (GNN), and anomaly detection models.

This project was built as part of a hackathon to address pressing environmental challenges using cutting-edge IoT and AI technology.

---
 Key Features

-  IoT-based data collection with ESP32, pH, and DO sensors
-  Graph Neural Networks for spatial pollution source tracing
-  LSTM-based prediction for pollution trends
-  Anomaly detection for identifying unusual pollution spikes
-  Real-time dashboard using **Streamlit**
-  Scalable architecture with **LoRaWAN** and drone surveillance support

---

## Tech Stack

- **Python** (Data processing & modeling)
- **Streamlit** (Dashboard UI)
- **ESP32**, **pH & DO Sensors** (Hardware integration)
- **FastAPI** or **CSV-based ingestion** (for data collection pipeline)
- **Graph Neural Networks (PyTorch Geometric)**
- **LSTM Models (TensorFlow/Keras)**
- **LoRaWAN & Drone APIs** (for future scalability)

---


git clone https://github.com/lichaa25/hackathon.git
cd pollutrack

set up the python environment
pip install -r requirements.txt


Run the streamlit dashboard
streamlit run app.py
for Iot simulatuion use the simulated_data.csv file or stream from a local fastAPI server

Sensor and data pipeline
[ESP32 + Sensors] → [LoRaWAN/FastAPI] → [Data Ingestion] → [Anomaly Detection + GNN] → [Streamlit Dashboard]

 contributors-
 Licha Gogoi
