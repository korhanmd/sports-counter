import math
 
def calculate_angle(p1, p2, p3):
    ang = math.degrees(math.atan2(p3[1]-p2[1], p3[0]-p2[0]) - math.atan2(p1[1]-p2[1], p1[0]-p2[0]))
    return ang + 360 if ang < 0 else ang