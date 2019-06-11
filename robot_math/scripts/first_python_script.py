import numpy as np
import pandas as pd
np.zeros((3,4))
A=np.ones((3,3))
I=np.eye(3)
np.empty((3,3))
X=np.array([[1,2,3],[2,2,2],[3,3,3]])
Y=np.array([[1,5,2],[0,0,0],[0,0,0]])

v=np.array([[1],[3],[0]])
X@v
XI=np.linalg.pinv(X)
XI@I

def rotx(angle,type="rad"):
    if type=="deg":
        R=np.array([[np.cos(np.deg2rad(angle)),-np.sin(np.deg2rad(angle)),0],[np.sin(np.deg2rad(angle)),np.cos(np.deg2rad(angle)),0],[0,0,1]])
    else:
        R=np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
    return R

R=rotx(30,"deg")
print(R)
