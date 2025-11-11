# ======================================================
# 🎵 Gesture-Controlled Music Player (Local Python)
# ======================================================

import cv2
import mediapipe as mp
import pygame
import os
import random

# ---------------- Music Setup ----------------
MUSIC_FOLDER = "MUSIC"  # Folder where your music files are stored

# Create the folder if it doesn't exist
if not os.path.exists(MUSIC_FOLDER):
    os.makedirs(MUSIC_FOLDER)
    print(f"Folder '{MUSIC_FOLDER}' created. Please add your .mp3 or .wav files there!")

# Use absolute path to avoid errors
MUSIC_FOLDER_PATH = os.path.abspath(MUSIC_FOLDER)

# List all music files
songs = [os.path.join(MUSIC_FOLDER_PATH, f) for f in os.listdir(MUSIC_FOLDER_PATH)
         if f.endswith(('.mp3', '.wav'))]

if not songs:
    print(f"⚠️ No music files found in '{MUSIC_FOLDER_PATH}'. Add music and restart the script.")
    exit()

current_song_index = 0
pygame.mixer.init()

def play_music():
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()
    print(f"🎶 Playing: {os.path.basename(songs[current_song_index])}")

def stop_music():
    pygame.mixer.music.stop()
    print("🛑 Music stopped")

def next_music():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_music()
    print(f"⏭ Next song: {os.path.basename(songs[current_song_index])}")

# ---------------- MediaPipe Setup ----------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# ---------------- Webcam Setup ----------------
cap = cv2.VideoCapture(0)
print("✅ Webcam started. Press 'Esc' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to capture frame from webcam.")
        break

    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    gesture_text = "None"

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            lm = handLms.landmark
            thumb_tip = lm[4]
            index_tip = lm[8]
            middle_tip = lm[12]
            ring_tip = lm[16]
            pinky_tip = lm[20]

            # --- Gesture Logic ---
            if thumb_tip.y < index_tip.y and thumb_tip.y < middle_tip.y:
                gesture_text = "👍 PLAY"
                if not pygame.mixer.music.get_busy():
                    play_music()
            
            elif all(f.y < lm[0].y for f in [index_tip, middle_tip, ring_tip, pinky_tip]):
                gesture_text = "✋ STOP"
                if pygame.mixer.music.get_busy():
                    stop_music()
            
            elif index_tip.y < middle_tip.y and middle_tip.y < ring_tip.y:
                gesture_text = "👆 NEXT"
                next_music()

    # Overlay gesture text on webcam feed
    cv2.putText(frame, f"Gesture: {gesture_text}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Gesture Music Player", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()
