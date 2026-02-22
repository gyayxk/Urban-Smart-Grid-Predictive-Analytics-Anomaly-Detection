⚡ Urban Smart Grid: Predictive Analytics & Anomaly Detection
Academic Thesis Project
Title: A Hybrid Deep Learning and Unsupervised Machine Learning Framework for Smart Energy Grid Monitoring.

📖 Project Overview
This project presents a robust, end-to-end intelligence system for modern urban energy grids. It addresses two critical challenges in power management: Load Forecasting and Security Monitoring. By combining a Transformer-based Neural Network for temporal predictions and an Isolation Forest for real-time anomaly detection, the system can automatically identify energy theft, meter tampering, and hardware failures.

🛠️ System Architecture & Modules
The project is designed with a modular architecture to ensure scalability and ease of integration:

 Module	            Component	                                 Role
main.py      	 The Orchestrator	The central engine that polls the database, triggers the AI models, and outputs real-time grid status.
simulator.py	 The Edge Layer	    Acts as a digital twin for smart meters, streaming kW and temperature data with synthetic anomalies.
dashboard.py	 The UI Layer	    A web-based Streamlit interface providing real-time visualization and business intelligence metrics.
train.py	     The Trainer	        Handles the optimization of the Transformer model and saves the weights as .pth files.
model.py	     The Forecaster	    Defines the Transformer architecture using multi-head self-attention for sequence modeling.
analytics.py	 The Detector	    Implements the Isolation Forest algorithm to flag statistical outliers (theft/faults).
database.py	     The Storage	        Manages the SQL schema and data persistence using SQLAlchemy.

🚀 Execution Guide
1. Environment Setup

# Clone the repository
git clone https://github.com/gyayxk/smart-grid-analytics.git
cd smart-grid-analytics

# Create and activate virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate

# Install dependencies
pip install torch scikit-learn pandas sqlalchemy streamlit plotly

Gemini said
This updated README is designed to look highly professional for both your Thesis Appendix and your GitHub repository. It emphasizes the academic nature of the project while providing clear technical instructions.

Save this as README.md in your main project folder.

⚡ Urban Smart Grid: Predictive Analytics & Anomaly Detection
Academic Thesis Project
Title: A Hybrid Deep Learning and Unsupervised Machine Learning Framework for Smart Energy Grid Monitoring.

📖 Project Overview
This project presents a robust, end-to-end intelligence system for modern urban energy grids. It addresses two critical challenges in power management: Load Forecasting and Security Monitoring. By combining a Transformer-based Neural Network for temporal predictions and an Isolation Forest for real-time anomaly detection, the system can automatically identify energy theft, meter tampering, and hardware failures.

🛠️ System Architecture & Modules
The project is designed with a modular architecture to ensure scalability and ease of integration:

Module	Component	Role
main.py	The Orchestrator	The central engine that polls the database, triggers the AI models, and outputs real-time grid status.
simulator.py	The Edge Layer	Acts as a digital twin for smart meters, streaming kW and temperature data with synthetic anomalies.
dashboard.py	The UI Layer	A web-based Streamlit interface providing real-time visualization and business intelligence metrics.
train.py	The Trainer	Handles the optimization of the Transformer model and saves the weights as .pth files.
model.py	The Forecaster	Defines the Transformer architecture using multi-head self-attention for sequence modeling.
analytics.py	The Detector	Implements the Isolation Forest algorithm to flag statistical outliers (theft/faults).
database.py	The Storage	Manages the SQL schema and data persistence using SQLAlchemy.
🚀 Execution Guide
1. Environment Setup
Bash
# Clone the repository
git clone https://github.com/yourusername/smart-grid-analytics.git
cd smart-grid-analytics

# Create and activate virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate

# Install dependencies
pip install torch scikit-learn pandas sqlalchemy streamlit plotly

2. Operational Workflow
To run the full demonstration, follow these steps in separate terminals:

Initialize Database: python database.py

Start Data Stream: python simulator.py (Let it run for 3-5 minutes to gather training data).

Train AI Model: python train.py (This generates the transformer_weights.pth file).

Launch Real-Time Monitor: python main.py

View Web Dashboard: streamlit run dashboard.py

📊 Key Research Features

Predictive Load Forecasting: Uses attention mechanisms to prioritize significant past events (e.g., peak hours) for future predictions.

Zero-Day Anomaly Detection: Identifies theft patterns without needing labeled historical theft data (Unsupervised Learning).

Economic Impact Analysis: The dashboard automatically calculates the estimated financial loss caused by detected anomalies.

Scalable SQL Backend: Capable of handling thousands of telemetry records with full audit logging.

🎓 Thesis Citation
If you use this project for your research or academic work, please cite it as:

Gyayak Jain, "AI-Driven Urban Smart Grid: Predictive Analytics & Anomaly Detection," Bachelor Of Technology Thesis, 2026.