import math
import cv2

def calculate_angle(point1, point2, point3):
    ang = math.degrees(math.atan2(point3[1]-point2[1], point3[0]-point2[0])
                       - math.atan2(point1[1]-point2[1], point1[0]-point2[0]))
    return ang + 360 if ang < 0 else ang

def write_angle(image, angle):
	# font
    font = cv2.FONT_HERSHEY_SIMPLEX

	# org
    org = (50, 50)

	# fontScale
    font_scale = 1

	# Blue color in BGR
    color = (255, 0, 0)

	# Line thickness of 2 px
    thickness = 2

	# Using cv2.putText() method
    cv2.putText(image, "{0:.2f}".format(angle), org, font,
                font_scale, color, thickness, cv2.LINE_AA)
    