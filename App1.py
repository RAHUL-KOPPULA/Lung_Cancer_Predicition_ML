import streamlit as st
import numpy as np
import joblib
import webbrowser
import base64

# ========== Page Config ==========
st.set_page_config(layout="wide")

# ========== Login Setup ==========
users = {
    "rahul@gmail.com": "abc@123",
    "user@info.in": "pass456"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# Centering with custom CSS
st.markdown(
    """
    <style>
        .login-container {
            display: flex;
            justify-content: Top;
            align-items: Top;
            height: 10vh; /* Adjust height as needed */
        }
        
    </style>
    """,
    unsafe_allow_html=True
)

# ========== Login Page ==========
if not st.session_state.logged_in:
    st.markdown('<div class="login-container"><div class="login-box">', unsafe_allow_html=True)

    st.title("🔐 User Login")
    st.markdown("Please login to access the Lung Cancer Prediction App.")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    login_col, forgot_col = st.columns(2)

    with login_col:
        if st.button("Login"):
            if email in users and users[email] == password:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid email or password.")

    with forgot_col:
        if st.button("Forgot Password?"):
            if email in users:
                st.info(f"ℹ️ Password reset instructions sent to {email} (simulated).")
            else:
                st.warning("⚠️ Email not found.")

    st.markdown('</div></div>', unsafe_allow_html=True)
    st.stop()

# ========== Load Model and Scaler ==========
try:
    model = joblib.load("lung_cancer_model.pkl")
    scaler = joblib.load("scaler.pkl")
except:
    st.error("❌ Error loading model or scaler.")
    st.stop()

# ========== Background Image CSS ==========
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_path = "C:/Users/RAHUL BABU KOPPULA/OneDrive/Desktop/3d-graphic-of-the-lung-and-human-body-hero.jpg"
img_base64 = get_base64(img_path)

st.markdown(f"""
<style>
body {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-attachment: fixed;
}}

section[data-testid="stSidebar"] > div {{
    background-color: rgba(0, 0, 0, 0.5);
}}

.card {{
    background-color: rgba(0, 0, 0, 0.75);
    padding: 1.5rem;
    border-radius: 1rem;
    color: white;
    margin-bottom: 1.5rem;
}}

footer {{
    text-align: center;
    color: white;
    font-size: 0.9rem;
    margin-top: 2rem;
}}
</style>
""", unsafe_allow_html=True)

# ========== Header ==========
st.markdown(f"<div class='header-left'style='font-size:60px;' >🎯 Welcome, <span style='color:#4da6ff'>{st.session_state.user_email}</span></div>", unsafe_allow_html=True)

# ========== Symptoms ==========
severity_map = {"Less": 1, "Moderate": 2, "Heavy": 3}
st.markdown("<hr style='border: 1px solid #aaa;'>", unsafe_allow_html=True)
st.markdown("<h3 style='color:white;'>🩺 Symptoms (Select Severity)</h3>", unsafe_allow_html=True)

symptom_col1, _ = st.columns([4, 1])  # 80% + 20%

with symptom_col1:
    col1, col2 = st.columns(2)
    with col1:
        symptom1 = st.selectbox("Coughing of Blood", ["Less", "Moderate", "Heavy"])
        symptom2 = st.selectbox("Chest Pain", ["Less", "Moderate", "Heavy"])
        symptom3 = st.selectbox("Shortness of Breath", ["Less", "Moderate", "Heavy"])

    with col2:
        symptom4 = st.selectbox("Fatigue", ["Less", "Moderate", "Heavy"])
        symptom5 = st.selectbox("Dry Cough", ["Less", "Moderate", "Heavy"])
        symptom6 = st.selectbox("Weight Loss", ["Less", "Moderate", "Heavy"])

inputs = [severity_map[symptom1], severity_map[symptom2], severity_map[symptom3],
          severity_map[symptom4], severity_map[symptom5], severity_map[symptom6]]

# ========== Layout ==========
left, center, right = st.columns([1.2, 1.5, 1.2])

with left:
    st.subheader("📁 Medical History")
    disease_history = st.text_input("Any previous diseases?")
    st.subheader("👨‍⚕️ Find Specialists")
    disease_specialist = st.text_input("E.g., cardiologist, Dermatologist")
    if st.button("🧑‍⚕️ Consult Nearby Doctors"):
        webbrowser.open(f"https://www.google.com/search?q={disease_specialist}+specialist+near+me")

with center:
    st.subheader("🔍 Predict Risk Level")
    padded_input = inputs + [1] * (23 - len(inputs))
    if st.button("📊 Predict"):
        scaled_input = scaler.transform([padded_input])
        prediction = model.predict(scaled_input)[0]
        risk_level = ["Low Risk", "Medium Risk", "High Risk"][int(prediction)]
        st.success(f"🚨 **Predicted Risk Level:** {risk_level}")

with right:
    with st.expander("📝 Feedback"):
        feedback = st.text_area("Your feedback:")
        if st.button("📤 Submit Feedback"):
            if feedback:
                st.success("✅ Thanks for your feedback!")
            else:
                st.warning("⚠️ Feedback is empty.")

    with st.expander("🐞 Report an Issue"):
        issue = st.text_area("Describe the issue:")
        if st.button("🚨 Submit Issue"):
            if issue:
                st.success("🛠️ We'll look into it.")
            else:
                st.warning("⚠️ Please describe the issue.")

# ========== Logout ==========
st.markdown("""
    <div class='logout-bottom'>
        <form action="?">
            <button type="submit">🔓 Logout</button>
        </form>
    </div>
""", unsafe_allow_html=True)

# ========== Footer ==========
st.markdown("<div class='custom-footer'>Developed by Koppula Rahul Babu</div>", unsafe_allow_html=True)