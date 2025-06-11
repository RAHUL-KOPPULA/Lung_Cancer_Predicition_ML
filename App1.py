import json, os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import joblib
import numpy as np
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(minutes=15)

USER_FILE = 'users.json'

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# Load model and scaler
model = joblib.load("model/lung_cancer_model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route('/')
def home():
    if 'logged_in' in session:
        return redirect(url_for('predict'))
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    users = load_users()
    email = request.form['email']
    password = request.form['password']
    if email in users and users[email] == password:
        session.permanent = True
        session['logged_in'] = True
        session['email'] = email
        return redirect(url_for('predict'))
    else:
        flash("❌ Invalid email or password.", "error")
        return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register():
    email = request.form['new_email']
    password = request.form['new_password']
    users = load_users()
    if email in users:
        flash("⚠️ Account already exists!", "error")
    else:
        users[email] = password
        save_users(users)
        flash("✅ Account created! Please log in.", "info")
    return redirect(url_for('home'))

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    email = request.form['forgot_email']
    users = load_users()
    if email in users:
        flash(f"📩 Simulated reset link: /reset-password/{email}", "info")
    else:
        flash("⚠️ Email not found.", "error")
    return redirect(url_for('home'))

@app.route('/reset-password/<email>', methods=['GET', 'POST'])
def reset_password(email):
    users = load_users()
    if request.method == 'POST':
        new_password = request.form['new_password']
        users[email] = new_password
        save_users(users)
        flash("🔒 Password reset successfully.", "info")
        return redirect(url_for('home'))
    return render_template("reset_password.html", email=email)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'logged_in' not in session:
        return redirect(url_for('home'))

    prediction = None
    if request.method == 'POST':
        severity_map = {"Less": 1, "Moderate": 2, "Heavy": 3}
        inputs = [
            severity_map[request.form['symptom1']],
            severity_map[request.form['symptom2']],
            severity_map[request.form['symptom3']],
            severity_map[request.form['symptom4']],
            severity_map[request.form['symptom5']],
            severity_map[request.form['symptom6']],
        ]
        padded_input = inputs + [1] * (23 - len(inputs))
        scaled_input = scaler.transform([padded_input])
        pred = model.predict(scaled_input)[0]
        risk_levels = ["Low Risk", "Medium Risk", "High Risk"]
        prediction = risk_levels[int(pred)]

    return render_template("predict.html", email=session['email'], prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
