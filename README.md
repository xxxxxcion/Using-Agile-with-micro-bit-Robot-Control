\# 🤖 Project Robot: Face Recognition with Micro:bit \& AI Lens



\*\*Semester 4 IoT Project\[Chen Xin]  

\*\*ID:\*\* \[202383890002]



\## 📖 Project Overview

This project implements an intelligent \*\*Face Recognition Robot\*\* using the \*\*Micro:bit V2\*\* and a \*\*K210 AI Camera (AI Lens)\*\*. The system uses Computer Vision to detect faces, extract features for identity matching, and communicates the result to the Micro:bit via UART Serial protocol.



The project was developed using \*\*Agile Methodology (Scrum)\*\* over 3 Sprints, utilizing GitHub for version control.



---



\## 🚀 Key Features

\* \*\*Real-time Face Detection:\*\* Uses YOLOv2 model on K210 AI Lens.

\* \*\*Identity Recognition:\*\* Matches face features against a registered database.

\* \*\*Privacy Protection:\*\* Implements \*\*Feature Hashing\*\* (storing vector data instead of raw images) to ensure data privacy.

\* \*\*Visual Feedback:\*\* Micro:bit LED matrix displays the user ID ("1", "2") or status icons.



---



\## 🛠️ Hardware Requirements

\* \*\*Micro:bit V2\*\* (Main Controller)

\* \*\*AI Lens / K210 Module\*\* (Vision Processing)

\* \*\*Robot Chassis\*\* (with Motors \& Wheels)

\* \*\*Expansion Board\*\* (for I2C/UART connection)



---



\## 📂 Source Code Description



\### 1. AI Vision Module (`face\_recognition\_k210.py`)

> \*\*Runs on:\*\* AI Lens (K210)  

> \*\*Function:\*\* > \* Loads YOLO and Feature Extraction models.

> \* Detects faces and compares them with stored features.

> \* Sends protocol data (e.g., `$08Y01,#`) via Serial/UART.



\### 2. Robot Control Module (`microbit\_display.py`)

> \*\*Runs on:\*\* Micro:bit V2  

> \*\*Function:\*\* > \* Receives UART signals from the camera.

> \* Parses the ID (e.g., "01", "02").

> \* Displays the corresponding number on the LED Matrix.



---



\## 📅 Agile Development Process



\### Sprint 1: Foundation

\* Hardware assembly.

\* Basic Micro:bit LED display logic.



\### Sprint 2: Core Logic

\* Implemented Face Recognition algorithms.

\* Established UART communication.



\### Sprint 3: Security \& Finalization

\* Added \*\*Data Hashing\*\* for privacy.

\* Final testing and documentation.



---



\## ⚙️ How to Run

1\.  \*\*AI Lens:\*\* Upload `face\_recognition\_k210.py` and the model files (`.kmodel`) to the AI Lens using the K-Flash or IDE tool.

2\.  \*\*Micro:bit:\*\* Flash `microbit\_display.py` to the Micro:bit using Mu Editor or Python Editor.

3\.  \*\*Connect:\*\* Ensure the Camera TX/RX pins are connected to the Micro:bit's mapped pins.

4\.  \*\*Start:\*\* Power on the robot. Press the BOOT key on the camera to register a face.

