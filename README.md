# Clamp Detection & Tracking using YOLOv11m

A Computer Vision project for detecting, tracking, and counting metal clamps mounted on a rotating industrial disk using YOLOv11m and object tracking techniques.

---

# 📌 Project Overview

This project was developed as part of a Computer Vision detection and tracking task. The main objective is to build an AI model capable of:

- Detecting metal clamps accurately
- Tracking clamps while the disk is rotating
- Counting detected clamps in real time
- Generating an annotated output video

The system uses a custom annotated dataset and a YOLOv11m model trained using the Ultralytics framework.

---

# 🎯 Objectives

The project focuses on solving multiple computer vision tasks simultaneously:

- Object Detection
- Multi-object Tracking
- Real-time Counting
- Video Processing
- Custom Dataset Training

The final output demonstrates stable clamp tracking and counting across video frames.

---

# 🧠 Technologies Used

- Python
- YOLOv11m
- Ultralytics
- OpenCV
- Roboflow
- Google Colab

---

# 📂 Dataset Preparation

## Frame Extraction
- Extracted 30 different frames from the provided rotating disk video.
- Selected frames from different disk positions to improve model generalization.
- Avoided blurry frames and low-quality samples.

## Annotation
- Annotated all visible clamps manually using Roboflow.
- Each clamp was labeled using a single class:

```text
clamp
Dataset Split

The dataset was divided into:

80% Training
15% Validation
5% Testing
Dataset Export
Exported in YOLO format
No resizing
No augmentation
🚀 Model Training

The model was trained using YOLOv11m with custom hyperparameters optimized for small moving objects.

Training Configuration
Parameter	Value
Model	YOLOv11m
Epochs	100
Image Size	640
Batch Size	8
Optimizer	AdamW
Framework	Ultralytics
🔍 Detection & Tracking Pipeline

The pipeline consists of the following stages:

Video Input
Frame Processing
Clamp Detection using YOLOv11m
Clamp Tracking using persistent IDs
Real-time Clamp Counting
Output Video Generation

The tracking system ensures that clamps remain tracked consistently while the disk rotates.

📊 Features
Real-time clamp detection
Object tracking across frames
Persistent tracking IDs
Clamp counting overlay
Video annotation generation
Custom dataset training
Industrial rotating object analysis
🖼️ Example Output

The generated output video includes:

Bounding boxes around detected clamps
Clamp IDs
Real-time clamp count
Continuous tracking during disk rotation📁 Project Structure

▶️ Training

Run model training:

python train.py
▶️ Inference & Tracking

Run detection and tracking on video:

python inference.py

The output video will be generated automatically.

📈 Challenges Faced

Several challenges were encountered during development:

Small object detection
Motion blur caused by disk rotation
Detection instability across frames
Limited dataset size
Tracking consistency

These issues were improved through:

Better annotation quality
Retraining the model
Confidence threshold tuning
Tracking persistence techniques
🔥 Future Improvements

Possible future enhancements include:

Increasing dataset size
Adding data augmentation
Using ByteTrack/DeepSORT
Kalman Filter smoothing
Real-time camera deployment
Industrial automation integration
👨‍💻 Author

Mohamed Salah

AI & Computer Vision Engineer

Interested in Artificial Intelligence, Computer Vision, and AI Automation
Focused on building real-world AI systems and industrial AI applications
