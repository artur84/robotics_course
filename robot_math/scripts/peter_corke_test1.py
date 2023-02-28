import roboticstoolbox as rtb
robot = rtb.models.Panda()
print(robot)
from spatialmath.base import *
q = qqmul([1,2,3,4], [5,6,7,8])
print(q)