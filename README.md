# House Price Prediction ML - Chennai & Bengaluru

A Flask-based Machine Learning web application that predicts house prices in Chennai and Bengaluru using Linear Regression and XGBoost with an interactive and user-friendly interface.

[![Repository](https://img.shields.io/badge/GitHub-kishore459%2FHouse--Price--Prediction--ML-blue?logo=github)](https://github.com/kishore459/House-Price-Prediction-ML)
[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-brightgreen?logo=python)](https://python.org)
[![Framework](https://img.shields.io/badge/Framework-Flask-black?logo=flask)](https://flask.palletsprojects.com/)

---

## 🚀 Features

- **🌐 Interactive Multi-City Valuation**: Real-time property valuation specifically tailored for Chennai and Bengaluru real estate markets.
- **🏢 Chennai House Predictor (`/chennai`)**: Calculates market prices based on square footage, BHK count, bathrooms, property age, construction status, builders, and prominent localities (Adyar, Velachery, Anna Nagar, OMR, etc.).
- **🏙️ Bengaluru House Predictor (`/bengaluru`)**: Fast property valuations for tech hubs and residential areas including Whitefield, Indiranagar, Electronic City, Koramangala, and HSR Layout.
- **⚡ Direct & Frictionless Access**: Simple and fast workflow allowing instant calculations without mandatory signups.
- **📱 Modern Responsive UI**: Sleek, responsive design that works seamlessly across desktop, tablet, and mobile browsers.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Gunicorn
- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Deployment**: Render / Gunicorn WSGI

---

## 📁 Project Structure

```text
House-Price-Prediction-ML/
│
├── static/
│   ├── style.css             # Main stylesheet for responsive UI and styling
│   └── script.js             # JavaScript for handling forms and API requests
│
├── templates/
│   ├── home.html             # Home / Landing page
│   ├── chennai.html          # Chennai price predictor page
│   ├── bengaluru.html        # Bengaluru price predictor page
│   ├── dashboard.html        # Valuation dashboard interface
│   ├── login.html            # User login interface
│   ├── register.html         # User registration interface
│   └── forgot_password.html  # Password recovery interface
│
├── app.py                    # Flask application routes and prediction APIs
├── Procfile                  # Gunicorn server startup config for cloud deployment
├── render.yaml               # Render blueprint configuration file
├── requirements.txt          # Required Python packages
└── README.md                 # Project documentation and guide
```

---

## 💻 Installation & Local Setup

1. **Clone Repository**:
   ```bash
   git clone https://github.com/kishore459/House-Price-Prediction-ML.git
   cd House-Price-Prediction-ML
   ```

2. **Activate Virtual Environment**:
   ```bash
   .\venv\Scripts\activate
   # or on macOS/Linux: source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**:
   ```bash
   python app.py
   ```

5. Open your browser at:
   - [http://127.0.0.1:5001/](http://127.0.0.1:5001/)

---

## ☁️ Deployment on Render

This project includes pre-configured `Procfile` and `render.yaml` for 1-click deployment on [Render](https://render.com):

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

---

## 👨‍💻 Author

- **GitHub**: [@kishore459](https://github.com/kishore459)
- **Repository**: [kishore459/House-Price-Prediction-ML](https://github.com/kishore459/House-Price-Prediction-ML)
