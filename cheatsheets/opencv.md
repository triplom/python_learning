# OpenCV Cheatsheet

## Installation & Import

```bash
pip install opencv-python
```

```python
import cv2
import numpy as np
print(cv2.__version__)
```

## Read / Write / Display

```python
img = cv2.imread("photo.jpg")           # BGR (not RGB!)
img = cv2.imread("photo.jpg", cv2.IMREAD_GRAYSCALE)  # grayscale

cv2.imwrite("output.png", img)
cv2.imshow("Window", img)               # needs display
cv2.waitKey(0)                          # wait for keypress
cv2.destroyAllWindows()

# Convert BGR → RGB for matplotlib
import matplotlib.pyplot as plt
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
```

## Color Spaces

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

## Drawing

```python
# rectangle(img, top_left, bottom_right, color_BGR, thickness)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# circle(img, center, radius, color, thickness; -1=filled)
cv2.circle(img, (cx, cy), r, (255, 0, 0), -1)

# line
cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

# text
cv2.putText(img, "Label", (x, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
```

## Resize, Crop, Flip

```python
small = cv2.resize(img, (320, 240))           # (width, height)
big   = cv2.resize(img, None, fx=2, fy=2)    # 2× scale
crop  = img[y1:y2, x1:x2]                    # numpy slice
flipped_h = cv2.flip(img, 1)                 # horizontal
flipped_v = cv2.flip(img, 0)                 # vertical
```

## Filters & Transformations

```python
blurred = cv2.GaussianBlur(img, (15,15), 0)
median  = cv2.medianBlur(img, 5)
edges   = cv2.Canny(gray, 50, 150)          # edge detection

# Threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
```

## Face Detection (Haar Cascade)

```python
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,    # image reduction per scale
    minNeighbors=5,     # required detections per rectangle
    minSize=(30, 30),   # minimum face size
)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
```

## Webcam / Video Capture

```python
cap = cv2.VideoCapture(0)          # 0 = default webcam; or "video.mp4"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process frame here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Webcam", gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

## Available Haar Cascades

```
haarcascade_frontalface_default.xml   # front face
haarcascade_frontalface_alt.xml       # front face (alt)
haarcascade_profileface.xml           # side face
haarcascade_eye.xml                   # eyes
haarcascade_smile.xml                 # smile
haarcascade_fullbody.xml              # full body
```

Path: `cv2.data.haarcascades + "filename.xml"`
