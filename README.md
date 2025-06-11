# Lung Cancer Risk Prediction Web App

🌟 **Advanced Machine Learning Web Application using Flask & Streamlit-inspired UI**

This project leverages machine learning to predict lung cancer risk levels based on clinical symptoms and lifestyle factors. It features a user-friendly web interface with secure login, interactive symptom selection, and doctor consultation support via Google search.

---

## 📈 Project Highlights

- ✅ ML model trained on real-world lung cancer datasets  
- ✅ Balanced classification using SMOTE to address class imbalance  
- ✅ Random Forest Classifier for accurate and robust predictions  
- ✅ Input features include six symptom severity levels (Coughing Blood, Chest Pain, Fatigue, etc.)  
- ✅ User authentication with registration, login, and password reset functionality  
- ✅ Responsive, clean UI with lung-cancer-themed background and accessibility focus  
- ✅ Google search integration for finding nearby specialists based on user input  
- ✅ Secure session handling and user-specific prediction history  
- ✅ Feedback and issue reporting forms integrated for user interaction  

---

## 🖥️ Technology Stack & Architecture

### Flask Backend
- **Flask** serves as the backend web framework powering user authentication, session management, and API endpoints.  
- Handles registration, login, logout, and password reset functionalities.  
- Loads and serves the trained machine learning model (`RandomForestClassifier`) and preprocessing scaler (`StandardScaler`).  
- Processes input symptoms, applies scaling, and returns risk predictions.

### Machine Learning Prediction Flow
- User inputs severity levels of six symptoms through dropdowns.  
- The backend converts these inputs into numeric features according to a severity map (Less=1, Moderate=2, Heavy=3).  
- Features are scaled using the loaded `StandardScaler` object to normalize input values.  
- The trained Random Forest model predicts lung cancer risk as one of three classes: Low, Medium, or High risk.  
- The predicted risk level is returned and displayed on the frontend.

### User Authentication & Security
- Users can **register** with any email and password combination stored in a JSON file (`users.json`).  
- Secure login verifies credentials against stored data.  
- Password reset functionality simulates email-based recovery steps.  
- Session management tracks logged-in users and restricts access to prediction features accordingly.  
- Logout endpoint clears sessions securely.  
- Frontend pages dynamically update based on login status for a personalized experience.

---

## 🧪 Model & Technical Details

- **Algorithm:** Random Forest Classifier with balanced class weights  
- **Preprocessing:** StandardScaler for feature normalization  
- **Imbalance Handling:** SMOTE (Synthetic Minority Oversampling Technique) applied during training  
- **Evaluation Metrics:** Precision, Recall, and F1-score ensuring reliable performance  
- **Prediction Output:** Multi-class classification with labels Low Risk, Medium Risk, High Risk  

---

## 🖥️ App Features

| Feature                       | Description                                         |
|------------------------------|-----------------------------------------------------|
| 🎛️ Symptom Severity Selection | Select severity levels for six key symptoms         |
| 📝 Medical History Input       | Enter previous diseases or conditions                |
| 📊 Real-time Risk Prediction   | Immediate lung cancer risk classification results    |
| 🌐 Specialist Search Button    | Search for relevant doctors nearby via Google       |
| 🔐 Secure User Login           | Register, login, and password reset with email validation |
| 📝 User Feedback & Bug Reporting | Provide feedback or report issues easily            |
| 🎨 Custom UI Design            | Themed background and accessible interface          |

---

## Author & Contact

**Koppula Rahul Babu**  
📧 Email: rahulrkgs34@gmail.com  

---

Feel free to reach out for collaboration, bug reports, or feature requests!
