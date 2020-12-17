"""
testts for measure module

"""

#imports
import pytest
import molecool
import numpy as np

def test_calculate_distance():
    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])

    expected_distance = 1

    calculate_distance = molecool.calculate_distance(r1,r2)

    assert expected_distance == calculate_distance

#test for calculate_angle_function
# use points (0,0,-1), (0,0,0), (1,0,0)
#expected angle 90

def test_calculate_angle():
    r1 = np.array([1,0,0])
    r2 = np.array([0,0,0])
    r3 = np.array([0,1,0])


    expected_value = 90

    calculate_angle = molecool.calculate_angle(r1,r2,r3, degrees = True)

    assert pytest.approx(expected_value) == calculate_angle

#decorator #need to write coorodinates
@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60  ),
    (np.array([np.sqrt(3)/2, (1/2), 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30),
])

def test_calculate_angle_many():
    calculate_angle = molecool.calculate_angle(p1,p2,p3, degrees = True)

    assert pytest.approx(expected_angle) == calculate_angle