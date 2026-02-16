## Esp32 S3 Hand Gesture RGB LED Controller

This project uses **computer vision + hand tracking** to control **LED colors on a microcontroller** via **serial communication**. Your hand gestures (number of raised fingers) are detected using **MediaPipe**, displayed in a **PyQt5 GUI**, and translated into color commands sent to an Arduino (or any serial-capable MCU).

### Video Demo

 [Video Demonstration](https://www.tiktok.com/@rycuadra24/video/7599141356899929362?is_from_webapp=1&sender_device=pc&web_id=7600738001065346580)

---
### How It Works

* OpenCV captures live video from your webcam
* MediaPipe detects and tracks one hand
* Fingers are counted based on landmark positions
* Each finger count maps to a color command
* The command is sent over Serial (USB)
* The microcontroller switches LEDs accordingly
* PyQt5 displays the live camera feed with overlays

---

### Finger-to-Color Mapping

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

### Requirements

### Hardware

* Webcam (any standard USB camera or built in on laptop)
* Esp32 S3 Devkit

### Software

* Python 3.10+
* OpenCV
* MediaPipe
* PyQt5
* PySerial

---

### Python Dependencies

Python Version Requirement

This project is developed and tested using Python 3.10.

Do not use Python 3.11, 3.12, or newer versions unless you know what you're doing.
Some MediaPipe and PyQt5 builds may break on newer interpreters.

Check your Python version:

```bash
python --version
```

If needed, install Python 3.10 from:
https://www.python.org/downloads/release/python-3100/

Install required libraries:

```bash
pip install opencv-python mediapipe pyqt5 pyserial
```

---

### Serial Configuration

Edit these lines to match your setup:

```python
SERIAL_PORT = "COM7"
BAUD = 115200
```
Make sure the baud rate matches your microcontroller firmware.

---


### Running the Program

```bash
python main.py
```

What you should see:

* A PyQt window with live camera feed
* Hand landmarks drawn on your hand
* Finger count + color text overlay
* LEDs changing color in real time
---
### Use Cases
* Touchless LED control
* Smart home demos
* Human-machine interaction experiments
* Computer vision learning projects
* Thesis or capstone demos
---
### License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for full details.

--- 

### Author

- Created with passion ❤ by: **Roy Cuadra**
- Updated Date: 02-16-2026

---

**Thank you for checking out this project!** 
You are welcome to **fork**, **improve**, or **use** it for learning purposes.
