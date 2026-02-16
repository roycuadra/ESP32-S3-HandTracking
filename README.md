## Esp32 S3 Hand Gesture RGB LED Controller

This project uses **computer vision + hand tracking** to control **LED colors on a microcontroller** via **serial communication**. Your hand gestures (number of raised fingers) are detected using **MediaPipe**, displayed in a **PyQt5 GUI**, and translated into color commands sent to an Arduino (or any serial-capable MCU).

---

## How It Works

* OpenCV captures live video from your webcam
* MediaPipe detects and tracks one hand
* Fingers are counted based on landmark positions
* Each finger count maps to a color command
* The command is sent over Serial (USB)
* The microcontroller switches LEDs accordingly
* PyQt5 displays the live camera feed with overlays

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

* Webcam (any standard USB camera or built in on laptop)
* Esp32 S3 Devkit

### Software

* Python 3.10+
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
Make sure the baud rate matches your microcontroller firmware.

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


---

## Use Cases

* Touchless LED control
* Smart home demos
* Human-machine interaction experiments
* Computer vision learning projects
* Thesis or capstone demos

---

## License

MIT License.

---

## Author

- roycuadra 2026
