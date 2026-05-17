from ultralytics import YOLO
import cv2

model = YOLO("best_model/best.pt")

video_path = "input.mp4"
cap = cv2.VideoCapture(video_path)

w = int(cap.get(3))
h = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter("output.mp4",
                       cv2.VideoWriter_fourcc(*"mp4v"),
                       fps, (w, h))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, persist=True, conf=0.15)[0]
    annotated = results.plot()

    count = len(results.boxes)

    cv2.putText(annotated, f"Clamps: {count}",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2)

    out.write(annotated)

cap.release()
out.release()
