from robopy import *
import numpy as np

x = UnitQuaternion.Rx(10, 'deg')
type(x)

y=UnitQuaternion.Ry(120,'deg')
x.animate(y,duration=15)

""" Compute Rotation Matrices
"""
Rx = rotx(90, 'deg')  # Rotation about the x-axis angle in degrees
print(Rx)
Ry = roty(np.pi)  # Rotation about the x-axis angle in degrees
print(Ry)

""" Compute Homogeneous Transformation Matrices
"""
TRot1= trotx(90, 'deg')  # Rotation about the x-axis angle in degrees
Trans1 = transl(1, 1, 2)
T1 = Trans1 * TRot1
print(T1)
# Simple form
# 2d Homogeneous transformation
T2= pose.SE2(theta=45, x=2, y=1, unit='deg')
print(T2)
# 3D Homogenous Transformation
T3 = pose.SE3.Rx(theta=45 , x=1, y= 0, z=0, unit='deg')
print(T3)

""" Animate a Puma robot
The following lines are used to start a simulation of a Puma560 robot
"""
robot = model.Puma560()
a = np.transpose(np.asmatrix(np.linspace(1, -180, 500)))
b = np.transpose(np.asmatrix(np.linspace(1, 180, 500)))
c = np.transpose(np.asmatrix(np.linspace(1, 90, 500)))
d = np.transpose(np.asmatrix(np.linspace(1, 450, 500)))
e = np.asmatrix(np.zeros((500, 1)))
f = np.concatenate((d, b, a, e, c, d), axis=1)
robot.animate(stances=f, frame_rate=30, unit='deg')

"""
"""
robot = model.Puma560()
robot.plot('qn')

"""
"""
