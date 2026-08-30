import os
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(BASE_DIR, "templates")
static_folder = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

# -------------------------------
# Home Page
# -------------------------------
@app.route('/')
def home():
    return render_template("home.html")


# -------------------------------
# Chennai Prediction Page
# -------------------------------
@app.route('/chennai')
def chennai():
    return render_template("chennai.html")


# -------------------------------
# Bengaluru Prediction Page
# -------------------------------
@app.route('/bengaluru')
def bengaluru():
    return render_template("bengaluru.html")


# =====================================================
# Chennai Prediction API
# =====================================================
@app.route('/predict/chennai', methods=['POST'])
def predict_chennai():
    data = request.get_json()

    area = float(data.get('area', 0))
    bhk = int(data.get('bhk', 0))
    bathroom = int(data.get('bathroom', 0))
    age = int(data.get('age', 0))

    # Prediction formula
    price = (
        area * 6500 +
        bhk * 500000 +
        bathroom * 200000 -
        age * 10000
    )

    return jsonify({
        "city": "Chennai",
        "predicted_price": round(price / 100000, 2),
        "unit": "Lakhs"
    })


# =====================================================
# Bengaluru Prediction API
# =====================================================
@app.route('/predict/bengaluru', methods=['POST'])
def predict_bengaluru():
    data = request.get_json()

    sqft = float(data.get('sqft', 0))
    bhk = int(data.get('bhk', 0))
    bath = int(data.get('bath', 0))
    age = int(data.get('age', 0))

    # Prediction formula
    price = (
        sqft * 7500 +
        bhk * 600000 +
        bath * 250000 -
        age * 12000
    )

    return jsonify({
        "city": "Bengaluru",
        "predicted_price": round(price / 100000, 2),
        "unit": "Lakhs"
    })


# -------------------------------
# Run Application
# -------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"Server started on http://127.0.0.1:{port}")
    app.run(debug=True, host="0.0.0.0", port=port)