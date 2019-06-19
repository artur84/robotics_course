from robopy import *
import numpy as np



""" Compute Rotation Matrices
"""
# 2D Rotations
R2=rot2(60,"deg")
print(R2)
# 3D Rotations
Rx = rotx(90, 'deg')  # Rotation about the x-axis angle in degrees
print(Rx)
Ry = roty(np.pi)  # Rotation about the x-axis angle in degrees
print(Ry)

""" Compute Homogeneous Transformation Matrices
"""
TRot1 = trotx(90, 'deg')  # Rotation about the x-axis angle in degrees
Trans1 = transl(1, 1, 2)
T1 = Trans1 * TRot1
print(T1)
# Simple form
# 2d Homogeneous transformation
T2 = pose.SE2(theta=45, x=2, y=1, unit='deg')
print(T2)

# 3D Homogenous Transformation
T3 = pose.SE3.Rx(theta=45, x=1, y=0, z=0, unit='deg')
print(T3)

""" Pose Multiplication
"""
x = pose.SE3.rand()
y = pose.SE3.rand()

z = x * y
print(z)
Rx
Ry
Rt=Rx*Ry
print(Rt)

""" Plot poses
"""
T3.plot()
T2.plot()

""" Animate a frame between two poses
"""
x = UnitQuaternion.Rx(10, 'deg')
y = UnitQuaternion.Ry(120, 'deg')
x.animate(y, duration=15)

""" Create a gif of a moving frame
"""
UnitQuaternion.Rx(45, 'deg').animate(duration = 15, gif = 'robot_math/scripts/qtGif')

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
