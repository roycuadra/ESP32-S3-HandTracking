import sys
import cv2
import mediapipe as mp
import serial
import time
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

# ---------------------- Serial Setup ----------------------
SERIAL_PORT = "COM7"
BAUD = 115200
ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
time.sleep(2)

# ---------------------- Mediapipe Setup ----------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# ---------------------- Finger Counting ----------------------
def count_fingers(hand_landmarks):
    tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
    pips = [6, 10, 14, 18]

    fingers = 0
    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers += 1
    # Other fingers
    for tip, pip in zip(tips, pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers += 1
    return fingers

finger_colors = {
    1: "GREEN",
    2: "BLUE",
    3: "RED",
    4: "VIOLET",
    5: "WHITE"
}

# ---------------------- PyQt5 GUI ----------------------
class HandControlGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hand LED Controller")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color:#1e1e1e; color:white; font-size:16px;")

        # Camera display
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # OpenCV video
        self.cap = cv2.VideoCapture(0)
        self.led_state = ""

        # Timer for updating frames
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_lm in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_lm, mp_hands.HAND_CONNECTIONS)
                fingers = count_fingers(hand_lm)
                color_cmd = finger_colors.get(fingers, "OFF")

                if self.led_state != color_cmd:
                    ser.write((color_cmd + "\n").encode())
                    self.led_state = color_cmd

                cv2.putText(frame, f"Fingers: {fingers} - {color_cmd}", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            if self.led_state != "OFF":
                ser.write(b"OFF\n")
                self.led_state = "OFF"
            cv2.putText(frame, "No Hand", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Convert to Qt image
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qt_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QPixmap.fromImage(qt_img))

    def closeEvent(self, event):
        # Release everything on close
        self.timer.stop()
        self.cap.release()
        ser.close()
        cv2.destroyAllWindows()
        event.accept()  # Close instantly

# ---------------------- Run App ----------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HandControlGUI()
    window.show()
    sys.exit(app.exec_())
