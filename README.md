# Real-Time-Detection-of-Object-Missing-and-New-Object-Placement-in-Video

This project focuses on building a real-time video analytics system capable of detecting two key scenarios:
1.	Missing Object Detection – Identifying when a previously visible object disappears from the scene.
2.	New Object Placement Detection – Identifying when a new object appears in the scene.
The primary goal is to create a reliable, high-performance pipeline for detecting these events as they occur, with real-time alerts displayed on the video feed. The system uses deep learning techniques for object detection and continuously processes video frames to ensure the analytics are accurate and timely.

# How It Works:
1.	Object Detection:
o	The project uses a YOLO (You Only Look Once) object detection model, which is a deep learning model optimized for real-time detection. YOLO processes each video frame to identify and classify objects.
o	The model outputs the object classes (e.g., car, person, dog) and their respective positions (bounding boxes) in the frame.
2.	Tracking Missing Objects:
o	The system keeps track of objects that were previously detected in earlier frames.
o	If an object that was previously detected disappears from the frame in subsequent video feeds, it is flagged as "missing".
o	A message such as "Missing Object: [Object Name]" is displayed on the screen, alerting the user of the absence.
3.	Detecting New Objects:
o	The system compares the current frame's objects with the ones detected in the previous frame.
o	Any object that appears for the first time in the current frame (but wasn't detected in the previous frame) is flagged as a "new object".
o	A message like "New Object Detected: [Object Name]" is displayed, notifying the user of the new presence.
4.	Real-Time Video Processing:
o	The pipeline processes each video frame in real-time using a webcam.
o	The FPS (Frames Per Second) rate is monitored to ensure that the detection system can run smoothly and efficiently. Although the FPS may vary depending on hardware (CPU vs. GPU), the system is designed to process and display results in real-time.

# download the yolov3.weights, yolov3.cfg, and the coco.names file from this link:
https://drive.google.com/drive/folders/177-gvbJ4WmD3TwQ14q1F1_0QKoBqlL5T?usp=sharing

# output video
https://drive.google.com/file/d/1v15u4pBEXRtNzUiiAqPhwq6cC87LNHGc/view?usp=drivesdk

# Report Link:
https://drive.google.com/file/d/1Yp2jOlV4KOstT6hehrFBLKkw7JRzzGc3/view?usp=sharing
