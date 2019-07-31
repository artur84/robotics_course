from fractions import Fraction as frac
from robopy import *
from numpy import *

"A simple script to compute general stuff"

print(frac(45, 54))
"""
"""
theta = arccos(-0.5)
print(theta)
I3 = eye(3)
Q = sqrt(5)  # theta
A = sin(Q) * array([[0, 0, 2], [0, 0, -1], [-2, 1, 0]])
B = (1 - cos(Q)) * array([[-4, 2, 0], [2, -1, 0], [0, 0, -5]])

print(I3 + A + B)
print(skew(matrix([1,2,3])))
print(I3 + (sin(Q)/Q) * skew(matrix([1, 2, 0])) + ((1 - cos(Q))/Q)
      * skew(matrix([1, 2, 0])) * skew(matrix([1, 2, 0])))
print(0.8660**2 + 0.5**2)
print(sqrt(1**2 + 2**2))
