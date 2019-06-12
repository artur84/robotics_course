import modern_robotics as mr
from robopy import *
import numpy as np

R = np.array([[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]])
invR = mr.RotInv(R)
print(invR)
x=UnitQuaternion.Rx(10,'deg')
type(x)
Rx=rotx(90,'deg')
print(Rx)
