import cv2
import mediapipe as mp

if __name__ == '__main__':
	mp_drawing  = mp.solutions.drawing_utils
	mp_pose = mp.solutions.pose
	cap = cv2.VideoCapture(0)

	if not cap.isOpened():
		print("Cannot open camera")
		exit()

	with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
		while True:
			# Capture frame-by-frame
			ret, frame = cap.read()

			# If frame is read correctly ret is True
			if not ret:
				print("Can't receive frame. Exiting...")
				break

			# Display the frame
			cv2.imshow('frame', frame)

			if cv2.waitKey(1) == ord('q'):
				break

		cap.release()
		cv2.destroyAllWindows()