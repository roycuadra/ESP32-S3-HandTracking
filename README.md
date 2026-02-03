# Hand Gesture LED Controller

This project uses **computer vision + hand tracking** to control **LED colors on a microcontroller** via **serial communication**. Your hand gestures (number of raised fingers) are detected using **MediaPipe**, displayed in a **PyQt5 GUI**, and translated into color commands sent to an Arduino (or any serial-capable MCU).

This is not magic. It is geometry, timing, and some clever abstractions stacked together.

---

## How It Works (High-Level)

* OpenCV captures live video from your webcam
* MediaPipe detects and tracks one hand
* Fingers are counted based on landmark positions
* Each finger count maps to a color command
* The command is sent over Serial (USB)
* The microcontroller switches LEDs accordingly
* PyQt5 displays the live camera feed with overlays

No cloud. No AI hype. Just real-time signal flow.

---

## Finger-to-Color Mapping

| Fingers Raised | Serial Command |
| -------------- | -------------- |
| 1              | GREEN          |
| 2              | BLUE           |
| 3              | RED            |
| 4              | VIOLET         |
| 5              | WHITE          |
| No hand        | OFF            |

The command is sent **only when the state changes**, preventing serial spam.

---

## Requirements

### Hardware

* Webcam (any standard USB camera)
* Arduino / ESP32 / ESP8266 (or similar)
* RGB LED or LED setup connected to MCU
* USB cable

### Software

* Python 3.8+
* OpenCV
* MediaPipe
* PyQt5
* PySerial

---

## Python Dependencies

Install required libraries:

```bash
pip install opencv-python mediapipe pyqt5 pyserial
```

---

## Serial Configuration

Edit these lines to match your setup:

```python
SERIAL_PORT = "COM7"
BAUD = 115200
```

Linux example:

```python
SERIAL_PORT = "/dev/ttyUSB0"
```

Make sure the baud rate matches your microcontroller firmware.

---

## Microcontroller Side (Important)

Your MCU firmware **must listen for newline-terminated strings**:

```text
GREEN
BLUE
RED
VIOLET
WHITE
OFF
```

A simple `Serial.readStringUntil('\n')` or equivalent is enough.

This project assumes **logic-level control**, not PWM color mixing (unless you implement it).

---

## Running the Program

```bash
python main.py
```

What you should see:

* A PyQt window with live camera feed
* Hand landmarks drawn on your hand
* Finger count + color text overlay
* LEDs changing color in real time

Latency is mostly camera-bound, not compute-bound.

---

## GUI Notes

* Built with PyQt5
* Uses QTimer for ~30 FPS updates
* Clean shutdown (camera + serial released properly)
* Dark theme for visibility

Close the window to safely terminate everything.

---

## Known Limitations

* Only **one hand** is tracked
* Thumb detection assumes **right hand orientation**
* Poor lighting reduces accuracy
* Webcam quality matters more than CPU power

This is physics, not vibes.

---

## Possible Improvements

* Left-hand support
* Gesture-based modes (fist, peace sign, etc.)
* PWM brightness control
* Bluetooth or Wi-Fi instead of USB
* Frame rate optimization using threading

---

## Use Cases

* Touchless LED control
* Smart home demos
* Human-machine interaction experiments
* Computer vision learning projects
* Thesis or capstone demos

---

## License

MIT License. Break it. Improve it. Learn from it.

---

## Author

Built by someone who prefers **signals over buzzwords**.
