from helper_functions import calculate_angle

class TestCalculateAngle:
    def test_1(self):
        assert calculate_angle([-1,0],[0,0],[1,0]) == 180.0

    def test_2(self):
        assert calculate_angle([-1,0],[0,0],[10,0]) == 180.0

    def test_3(self):
        assert calculate_angle([-1,0],[0,0],[1,1]) == 225.0

    def test_4(self):
        assert calculate_angle([1,0],[0,0],[1,0]) == 0.0

    def test_5(self):
        assert calculate_angle([1,-1],[0,0],[1,0]) == 45.0

    def test_6(self):
        assert calculate_angle([1,-1],[0,0],[1,1]) == 90.0
        