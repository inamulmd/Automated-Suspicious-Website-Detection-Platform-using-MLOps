## Automated Suspicious Website Detection Platform using MLOps

An end-to-end machine learning–based security system that detects suspicious / phishing websites using engineered URL security features and a production-style MLOps pipeline.
The project is designed as a backend ML service, exposed via FastAPI, following real-world ML engineering practices.

###📌 Problem Statement

Phishing and malicious websites are a daily cybersecurity threat.
Traditional blacklist-based systems fail to detect new and unseen malicious URLs.

This project solves that by:

Learning behavioral and structural patterns of malicious websites

Using machine learning models trained on security features

### Deploying the model as a scalable backend service

🚀 Key Features

✅ ML-based suspicious website detection

✅ Pre-engineered URL security feature dataset

✅ Modular, config-driven ML pipeline

✅ Model training, evaluation, and artifact management

✅ REST API for real-time inference (FastAPI)

✅ Designed with MLOps principles

✅ Ready for containerization & cloud deployment

###  Dataset Overview

The dataset consists of engineered URL security features, not raw URLs.

Each row represents a website using 30 security-related features, such as:

Presence of IP address

URL length

SSL status

Domain age

DNS records

Web traffic

Google index status

Redirection behavior

Target column:

Result → 1 (Legitimate) or -1 (Phishing)

⚠️ Feature engineering is assumed to be done offline.
This mirrors real-world ML systems where feature stores provide clean features.

🏗️ System Architecture
Dataset (CSV with security features)
        ↓
Data Validation & Transformation
        ↓
Model Training & Evaluation
        ↓
Model Artifacts (Preprocessor + Model)
        ↓
FastAPI Inference Service
        ↓
Prediction Output (JSON / UI)

 ### Tech Stack
Category	Tools
Language	Python
ML	Scikit-learn
Backend	FastAPI
Experiment Tracking	MLflow
Data Handling	Pandas, NumPy
Serialization	Joblib
Deployment Ready	Docker, GitHub Actions
Cloud (Planned)	AWS S3, ECR, EC2


### Project Structure
'''
Network_Security/
│
├── app.py                      # FastAPI application entry point
│
├── networksecurity/            # Core ML & pipeline logic
│   ├── components/             # Data ingestion, training, evaluation modules
│   ├── pipeline/               # Training & prediction pipelines
│   ├── utils/                  # Common utility functions
│   ├── exception/              # Custom exception handling
│   └── logger/                 # Centralized logging
│
├── final_model/                # Trained model artifacts
│   ├── model.pkl               # Trained ML model
│   └── preprocessor.pkl        # Feature preprocessing pipeline
│
├── templates/                  # UI templates (demo only)
│   └── table.html              # HTML table for prediction output
│
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration (planned)
├── .github/
│   └── workflows/              # CI/CD pipelines (planned)
│
└── README.md                   # Project documentation
'''

🔌 API Usage
🔹 Predict Suspicious Website (JSON API)

Endpoint

POST /predict


Input

Upload a CSV file with one row of feature values

Response

<img width="1319" height="614" alt="Screenshot 2026-02-03 160656" src="https://github.com/user-attachments/assets/6d94604a-0129-40dd-b4b4-03277827d7e1" />

<img width="1323" height="674" alt="Screenshot 2026-02-03 160708" src="https://github.com/user-attachments/assets/b7d848b1-16ed-4af3-a9d9-09afd80be2b4" />


⚠️ Designed for single-row real-time inference (not batch).

🔹 UI Demo Endpoint (Optional)

Endpoint

POST /predict-ui


Returns:

HTML table showing features + prediction

Useful for demos and presentations

⏱ Performance

Model loaded once at startup

Single-row inference latency: < 30 ms

Optimized for real-time usage

### How to Run Locally
# create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# start API server
uvicorn app:app --reload


Open:

http://127.0.0.1:8000/docs

🔐 MLOps & Deployment (Planned)

The following steps are designed and planned as part of the project roadmap:

☑️ Push trained model & artifacts to AWS S3

☑️ Dockerize the FastAPI application

☑️ CI/CD pipeline using GitHub Actions

☑️ Push Docker image to AWS ECR

☑️ Deploy service on AWS EC2

