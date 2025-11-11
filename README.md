# 🎵 Gesture-Controlled Music Player (Local Python)

Control your music **hands-free** using simple **AI-powered hand gestures**!  
This project uses **OpenCV** and **MediaPipe** to detect real-time hand gestures via webcam, allowing you to **Play**, **Stop**, or **Skip** songs without touching your keyboard.

---

## 🧠 Features
- ✋ **Play, Stop, and Next Song** gestures detected using webcam
- 🎶 Automatically scans and plays songs from the local **`MUSIC/`** folder
- 📷 Real-time **gesture recognition** powered by MediaPipe
- 🎧 Uses **Pygame** for smooth music playback
- 💡 Works completely **offline** — no internet required

---

## 🧰 Tech Stack
- **Language:** Python  
- **Libraries Used:**
  - `opencv-python` → For video capture and display  
  - `mediapipe` → For hand tracking and gesture detection  
  - `pygame` → For music playback  
  - `os`, `random` → For file handling and random song selection

---

## 🚀 How It Works
1. The camera captures your **hand** using OpenCV.  
2. **MediaPipe** detects hand landmarks (fingers, tips, etc.).  
3. Based on the finger positions:
   - 👍 **Thumbs Up** → Plays music  
   - ✋ **Open Palm** → Stops music  
   - 👆 **Pointing Up** → Plays next song  
4. The selected song is played using **Pygame’s mixer** module.

---

## 🖥️ Project Structure
