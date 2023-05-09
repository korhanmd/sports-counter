import math
import cv2

def calculate_angle(p1, p2, p3):
    ang = math.degrees(math.atan2(p3[1]-p2[1], p3[0]-p2[0]) - math.atan2(p1[1]-p2[1], p1[0]-p2[0]))
    return ang + 360 if ang < 0 else ang

def write_angle(image, angle):
	# font
    font = cv2.FONT_HERSHEY_SIMPLEX

	# org
    org = (50, 50)

	# fontScale
    fontScale = 1

	# Blue color in BGR
    color = (255, 0, 0)

	# Line thickness of 2 px
    thickness = 2

	# Using cv2.putText() method
    cv2.putText(image, "{0:.2f}".format(angle), org, font,
                fontScale, color, thickness, cv2.LINE_AA)
    