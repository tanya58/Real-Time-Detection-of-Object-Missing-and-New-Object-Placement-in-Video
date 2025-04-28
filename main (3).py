import cv2
import numpy as np

def detect_objects(frame, net, output_layers):
    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.4:  # Confidence threshold
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    return boxes, confidences, indexes, class_ids


def update_tracking(objects, frame):
    tracker = cv2.MultiTracker_create()
    for obj in objects:
        tracker.add(cv2.TrackerCSRT_create(), frame, tuple(obj))
    return tracker

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

cap = cv2.VideoCapture(0)  # Change to video file if needed

old_labels = []  # To track objects across frames

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Object detection
    boxes, confidences, indexes, class_ids = detect_objects(frame, net, output_layers)
    
    labels = [classes[class_ids[i]] for i in range(len(boxes)) if i in indexes]

    # Compare with previous labels to detect new or missing objects
    new_labels = [label for label in labels if label not in old_labels]
    missing_labels = [label for label in old_labels if label not in labels]

    if new_labels:
        print(f"New objects detected: {', '.join(new_labels)}")
        # Display on screen
        cv2.putText(frame, f"New: {', '.join(new_labels)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    if missing_labels:
        print(f"Missing objects: {', '.join(missing_labels)}")
        # Display on screen
        cv2.putText(frame, f"Missing: {', '.join(missing_labels)}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Update old labels for the next frame comparison
    old_labels = labels.copy()

    # Display bounding boxes for detected objects
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = np.random.uniform(0, 255, size=(3,))
            confi = round(confidences[i], 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {confi}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow("Object Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
