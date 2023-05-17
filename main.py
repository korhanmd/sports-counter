import cv2
import mediapipe as mp
import helper_functions

def get_current_state(current_state, angle1, angle2):
    threshold1 = 180
    threshold2 = 15

    if current_state == "down" and angle1 >= threshold1 and angle2 >= threshold2:
        current_state = "up"
    elif current_state == "up" and angle1 < threshold1 and angle2 < threshold2:
        current_state = "down"

    return current_state

if __name__ == '__main__':
    mp_drawing  = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture(0)
    state = "down"

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Detect pose landmarks
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)

			# If frame is read correctly ret is True
            if not ret:
                print("Can't receive frame. Exiting...")
                break

            try:
                landmarks = results.pose_landmarks.landmark

                shoulder_left   = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                wrist_left      = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                wrist_right     = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                hip_left        = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                ankle_left      = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                ankle_right     = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                angle_arms = helper_functions.calculate_angle(
                    wrist_left, shoulder_left, wrist_right)
                angle_legs = helper_functions.calculate_angle(
                    ankle_left, hip_left, ankle_right)

                state = get_current_state(state, angle_arms, angle_legs)

                helper_functions.write_angle(frame, angle_arms, (50, 50))
                helper_functions.write_angle(frame, angle_legs, (50, 100))
                cv2.putText(frame, state, (50, 150), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2, cv2.LINE_AA)
            except:
                pass

            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66),
                                    thickness=2, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(245,66,230),
                                    thickness=2, circle_radius=2)
                                )

			# Display the frame
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        