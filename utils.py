import cv2
import os

def extract_frames(video_path, output_folder="outputs/frames"):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % 30 == 0:
            cv2.imwrite(f"{output_folder}/frame_{count}.jpg", frame)

        count += 1

    cap.release()
    return output_folder