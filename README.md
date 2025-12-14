## 📂 Source Code Description

### 1. AI Vision & Privacy Module (`face_recognition_k210.py`)
> **Runs on:** AI Lens (K210)  
> **Function:** > * **Face Detection:** Uses YOLOv2 model.
> * **Privacy Protection:** Implements **Feature Extraction** to convert face images into mathematical vectors (Hashing) for storage, ensuring no raw photos are saved.
> * **Communication:** Sends protocol data (e.g., `$08Y01,#`) via Serial/UART.

### 2. Robot Control Module (`microbit_display.py`)
> **Runs on:** Micro:bit V2  
> **Function:** > * Receives UART signals from the camera.
> * Parses the ID (e.g., "01", "02").
> * Displays the corresponding number on the LED Matrix.
