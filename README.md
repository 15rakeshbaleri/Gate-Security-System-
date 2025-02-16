# AI-Powered Smart Gate Security System

## 📌 Overview
This project is an **AI-powered smart gate security system** that automates the entry process for pedestrians and vehicles using **Face Recognition, Car Plate Detection, and AI Voice Assistance**. The system ensures **fast, secure, and automated** access for employees and visitors.

---
## 🔧 Modules & Features

### 1️⃣ Face Recognition (For Walk-in Visitors)
- A camera scans the visitor’s face.
- If the person is recognized, entry is recorded.
- If unrecognized, the AI assistant collects visitor details.

✅ **Why is this useful?**
- Tracks every entry automatically.
- Reduces manual work for security personnel.
- Eliminates paper-based visitor logs.

### 2️⃣ Car Plate Detection (For Visitors with Vehicles)
- Captures the license plate using a camera.
- Checks the database for registered vehicles.
- Opens the gate automatically for recognized vehicles.
- Activates AI Voice Assistant if the vehicle is unregistered.

✅ **Why is this useful?**
- Eliminates the need for manual vehicle checks.
- Provides quick, automated access for employees.
- Maintains a digital log of all vehicle entries.

### 3️⃣ AI Voice Assistant (For New Visitors)
- If a visitor is neither recognized by face nor vehicle, the AI assistant asks for their **name, phone number, and purpose of visit**.
- The visitor responds verbally, and the system automatically fills out the form.
- The details are saved for future visits.

✅ **Why is this useful?**
- Simplifies visitor registration with voice input.
- Reduces manual data entry.
- Enhances security with a digital visitor log.

### 📊 Data Logging & Security Integration
- Every visitor (recognized or new) is **logged in the database**.
- Security personnel can review logs anytime for **monitoring and reporting**.

✅ **Why is this useful?**
- Provides a **secure** and **centralized** visitor database.
- Reduces the risk of unauthorized entry.
- Improves **tracking** and **security audits**.

---
## 📽 Demo Video
Watch the project in action:
[![Watch Video](https://drive.google.com/file/d/1_CzDhQ6jDR8dwGxJBBKnmOn-gKElBC7h/view?usp=sharing)

🔗 **Click [here](https://drive.google.com/file/d/1_CzDhQ6jDR8dwGxJBBKnmOn-gKElBC7h/view?usp=sharing) to watch the full video**

---
## 🛠 Technologies Used
- **Python** (OpenCV, YOLO, SpeechRecognition, PyTTSX3)
- **MongoDB** (For storing visitor & vehicle logs)
- **Flask** (For backend processing)
- **Machine Learning** (Face Recognition & License Plate Detection)

---
## 🚀 How to Run the Project
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/smart-gate-security.git
   cd smart-gate-security
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the system**
   ```bash
   python main.py
   ```

---
## 📩 Contact
For any queries or contributions, reach out to **[sangam gowda HM]** at **sangamgowdahm24@gmail.com**.
