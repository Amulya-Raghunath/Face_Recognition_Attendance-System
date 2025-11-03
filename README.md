# Face_Recognition_Attendance-System
A desktop-based Face Recognition Attendance System built using Python, OpenCV, and Tkinter, that automatically marks attendance through live facial recognition.
The system includes faculty authentication (face + login) to ensure secure attendance approval and prevent proxy attendance.

🚀 Key Features
Feature	Description
✅ LBPH Facial Recognition	Reliable & fast face identification
✅ Real-time Student Detection	Captures & verifies faces via webcam
✅ Faculty Face Authentication	Dual-layer security (login + face)
✅ Tkinter UI	Clean and simple desktop interface
✅ Attendance Logging	Stored in database (MySQL)
✅ Dataset Creation Module	Capture & store face images
✅ Model Training Script	Train LBPH recognizer on captured faces
🧠 Tech Stack
Component	Technology
Language	Python
GUI Framework	Tkinter
Face Recognition	OpenCV LBPHFaceRecognizer
Image Processing	OpenCV, NumPy
Database	MySQL 
Other Libraries	PIL, datetime, csv
🏗️ System Workflow

1️⃣ Student/Faculty face images are captured
2️⃣ LBPH algorithm trains a face recognition model
3️⃣ Face is detected via webcam in runtime
4️⃣ Model predicts identity → attendance is recorded
5️⃣ Faculty login & face match required to validate attendance
6️⃣ Data stored securely in database


