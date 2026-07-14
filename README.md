# Color-Recognition-using-OpenCV

## Project Description
This project demonstrates real-time color recognition using OpenCV and Python. The program captures live video from the webcam, detects blue-colored objects using the HSV color space, and highlights the detected object by drawing a bounding box around it.

## Features
- Real-time webcam video capture.
- Blue color detection using the HSV color model.
- Object tracking with a bounding rectangle.
- Displays the original camera feed, color mask, and detected object.

## Technologies Used
- Python
- OpenCV
- NumPy
- Anaconda
- Visual Studio Code

## Project Structure
```
OpenCV-Color-Recognition/
│
├── color_tracker.py
├── README.md
└── screenshots/
```

## Installation
1. Create or activate an Anaconda environment.
2. Install the required libraries:

```bash
pip install opencv-python numpy
```

## How to Run

Run the following command:

```bash
python color_tracker.py
```

## Output
The application will:
- Open the webcam.
- Detect blue-colored objects in real time.
- Display the detected object with a green bounding box.
- Show the original frame, color mask, and detection result.

## Future Improvements
- Support multiple colors.
- Display object coordinates and area.
- Improve tracking accuracy under different lighting conditions.

## Author
Developed as an OpenCV assignment using Python.
