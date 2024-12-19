import cv2
import mediapipe as mp
import threading
from calculate_angle import calculate_angle_from_nose_to_shoulders, calculate_angle_at_left_shoulder, calculate_angle_at_right_shoulder  # Import both functions

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

webcam_feed = cv2.VideoCapture(0)  

frame_count = 0  
processing_interval = 15  


landmarks_to_display = [
    0, 11, 12, 13, 14, 15, 16, 33, 263, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27
]
landmarks_printed = False  

ready_flag = False

def get_user_input(): 
    global ready_flag
    ready = input("Type 'start' to capture initial landmarks: ")
    if ready == 'start':
        ready_flag = True


input_thread = threading.Thread(target=get_user_input)
input_thread.start()

with mp_holistic.Holistic(min_detection_confidence=0.8, min_tracking_confidence=0.8) as holistic:
    
    while webcam_feed.isOpened():
        ret, frame = webcam_feed.read()

        frame_count += 1

        if not ret:
            continue

        
        display_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        
        results = holistic.process(display_image)

        if results.pose_landmarks:
            
            for idx in landmarks_to_display:
                if idx < len(results.pose_landmarks.landmark):  
                    landmark = results.pose_landmarks.landmark[idx]
                    if landmark:
                        x, y = int(landmark.x * display_image.shape[1]), int(landmark.y * display_image.shape[0])
                        cv2.circle(display_image, (x, y), 5, (0, 255, 0), -1)

            
            landmark_0 = results.pose_landmarks.landmark[0]  
            landmark_11 = results.pose_landmarks.landmark[11]  
            landmark_12 = results.pose_landmarks.landmark[12]  

            
            angle_degrees_1, (x0, y0), (x11, y11), (x12, y12) = calculate_angle_from_nose_to_shoulders(landmark_0, landmark_11, landmark_12, display_image)
            print(f"Angle between nose and shoulders: {angle_degrees_1:.2f} degrees")

            
            angle_degrees_2, (x11, y11), (x0, y0), (x12, y12) = calculate_angle_at_left_shoulder(landmark_0, landmark_11, landmark_12, display_image)
            print(f"Angle at left shoulder: {angle_degrees_2:.2f} degrees")

            
            angle_degrees_3, (x12, y12), (x0, y0), (x11, y11) = calculate_angle_at_right_shoulder(landmark_0, landmark_11, landmark_12, display_image)
            print(f"Angle at right shoulder: {angle_degrees_3:.2f} degrees")

            
            if angle_degrees_1 < 100 and angle_degrees_2 < 50 and angle_degrees_3 < 50:
                line_color = (0, 255, 0)  # Green if all conditions are met
            elif angle_degrees_1 >= 100:
                line_color = (255, 0, 0)  # Red if angle_degrees_1 condition violated
            elif angle_degrees_2 >= 50:
                line_color = (0, 0, 255)  # Blue if angle_degrees_2 condition violated
            elif angle_degrees_3 >= 50:
                line_color = (255, 0, 255)  # Purple if angle_degrees_3 condition violated
            else:
                line_color = (0, 0, 0)  # Black if none of the conditions are met

            
            cv2.line(display_image, (x0, y0), (x11, y11), line_color, 2)  
            cv2.line(display_image, (x0, y0), (x12, y12), line_color, 2)  
            cv2.line(display_image, (x11, y11), (x12, y12), line_color, 2)  

            
            cv2.putText(display_image, f"Nose-Shoulders: {angle_degrees_1:.2f}°", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(display_image, f"Left Shoulder: {angle_degrees_2:.2f}°", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(display_image, f"Right Shoulder: {angle_degrees_3:.2f}°", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        
        display_image = cv2.cvtColor(display_image, cv2.COLOR_RGB2BGR)

        # Save the frame for analysis at specified intervals
        #if frame_count % processing_interval == 0:
         #   cv2.imwrite(f"analysis_frame_{frame_count}.jpg", display_image)

        
        cv2.imshow('Holistic Model Detection', display_image)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

webcam_feed.release()
cv2.destroyAllWindows()
