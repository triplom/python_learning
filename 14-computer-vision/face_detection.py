# Computer Vision — OpenCV & Face Detection
# Course 7 (Detecção de Faces com Python e OpenCV)
# pip install opencv-python

import cv2
import numpy as np
import os

print(f"OpenCV version: {cv2.__version__}")

# ═══════════════════════════════════════
#  BASICS — Read, show, write images
# ═══════════════════════════════════════


def demo_basic_operations():
    """Create a synthetic image and demonstrate basic operations."""
    # Create a blank canvas (500×400, 3-channel BGR)
    img = np.zeros((400, 500, 3), dtype=np.uint8)

    # ─── Drawing ──────────────────────────────────────────────────────────────
    # rectangle(image, top_left, bottom_right, color_BGR, thickness)
    cv2.rectangle(img, (50, 50), (200, 150), (0, 255, 0), 3)  # green rect
    cv2.circle(img, (350, 100), 60, (255, 0, 0), -1)  # filled blue circle
    cv2.line(img, (0, 200), (500, 200), (0, 0, 255), 2)  # red horizontal line
    cv2.ellipse(
        img, (250, 300), (100, 50), 0, 0, 360, (255, 255, 0), 2
    )  # yellow ellipse

    # Text
    cv2.putText(
        img, "OpenCV Demo", (100, 380), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2
    )

    cv2.imwrite("opencv_basic.png", img)
    print("Saved: opencv_basic.png")

    # ─── Color spaces ─────────────────────────────────────────────────────────
    sample = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)
    print(f"Original shape: {sample.shape}")
    print(f"Grayscale shape: {gray.shape}")

    return img


# ═══════════════════════════════════════
#  FACE DETECTION — Haar Cascade
# ═══════════════════════════════════════


def detect_faces_in_image(image_path=None):
    """
    Detect faces using Haar cascade classifier.
    If no image path provided, creates a test image.
    """
    # Load pre-trained cascade (bundled with OpenCV)
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    print(f"Haar cascade loaded from: {cascade_path}")

    if image_path and os.path.exists(image_path):
        img = cv2.imread(image_path)
    else:
        # Synthetic demo image (gray rectangle = "face")
        img = np.ones((300, 300, 3), dtype=np.uint8) * 200
        print("No image provided — using synthetic placeholder")
        print("For real face detection, pass a path to a photo.")
        cv2.imwrite("face_detection_demo.png", img)
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    # scaleFactor: how much image size is reduced at each scale
    # minNeighbors: how many neighbors each rectangle should have
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    print(f"Faces detected: {len(faces)}")

    for x, y, w, h in faces:
        # Draw rectangle around face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            img, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
        )

        # Detect eyes within the face region
        face_gray = gray[y : y + h, x : x + w]
        face_color = img[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=5)
        for ex, ey, ew, eh in eyes:
            cv2.circle(
                face_color, (ex + ew // 2, ey + eh // 2), ew // 2, (255, 0, 0), 2
            )

    out_path = "face_detection_result.png"
    cv2.imwrite(out_path, img)
    print(f"Result saved: {out_path}")


# ═══════════════════════════════════════
#  VIDEO CAPTURE (real-time)
# ═══════════════════════════════════════


def face_detection_webcam():
    """
    Real-time face detection from webcam.
    Run this in an environment with a webcam and display.
    Press 'q' to quit.
    """
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    cap = cv2.VideoCapture(0)  # 0 = default webcam
    if not cap.isOpened():
        print("Cannot open webcam")
        return

    print("Press 'q' to quit webcam feed")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"Face {w}x{h}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

        cv2.putText(
            frame,
            f"Faces: {len(faces)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )
        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# ═══════════════════════════════════════
#  IMAGE PROCESSING TECHNIQUES
# ═══════════════════════════════════════


def image_processing_demo():
    # Create test image
    img = np.random.randint(0, 256, (200, 300, 3), dtype=np.uint8)

    # Blur (noise reduction — often applied before face detection)
    blurred = cv2.GaussianBlur(img, (15, 15), 0)
    median = cv2.medianBlur(img, 5)

    # Edge detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1=50, threshold2=150)

    # Resize
    small = cv2.resize(img, (150, 100))
    big = cv2.resize(img, None, fx=2, fy=2)

    print(f"Original: {img.shape}")
    print(f"Small:    {small.shape}")
    print(f"Big:      {big.shape}")

    cv2.imwrite("edges.png", edges)
    print("Edge detection saved: edges.png")


if __name__ == "__main__":
    demo_basic_operations()
    image_processing_demo()
    detect_faces_in_image()  # pass a photo path for real detection
    # face_detection_webcam()  # uncomment if webcam available

# LAB EXERCISES
# 1. Download a portrait photo. Run detect_faces_in_image() on it.
# 2. Add a counter overlay showing how many faces were detected.
# 3. Try the profileface cascade (haarcascade_profileface.xml) for side-profile faces.
# 4. (Advanced) Replace Haar cascade with DNN face detection using cv2.dnn.
