#!/usr/bin/env python
from spatialmath import SO3
import spatialmath.base as tr 
import sympy as sym
import numpy as np
from numpy.linalg import det
from numpy.linalg import inv

phi, Q, psi = sym.symbols('phi Q psi') #Create some symbolic variables

#Create a rotation matrix for Euler angles ZXZ
R=SO3.Rz(phi)*SO3.Rx(Q)*SO3.Rz(psi)
R.print()


#Create a Rotation matrix Rz(30)Rx(60)Rz(45)
R1=SO3.Rz(30,'deg')*SO3.Rx(60,'deg')*SO3.Rz(45,'deg')
R1.print()


#Create a Rotation matrix Rz(30)Rx(60)Rz(45)
R2=SO3.Rz(45,'deg')*SO3.Rx(60,'deg')*SO3.Rz(30,'deg')
R2.print()

#From R to Euler ZXZ
phi, Q, psi = sym.symbols('phi Q psi') #Create some symbolic variables
sx, sy, sz = sym.symbols('sx sy sz') #Create some symbolic variables
ax, ay, az = sym.symbols('ax ay az') #Create some symbolic variables
nx, ny, nz = sym.symbols('nx ny nz') #Create some symbolic variables

R=np.array([[sx, nx, ax],[sy, ny, ay],[sz, nz, az]])
print(R)

print(SO3.Rz(-phi)*R)
print(SO3.Rx(Q)*SO3.Rz(psi))

#Example ZXZ2 Compute ZXZ Euler Angles from Rotation Matrix

R1=np.array(SO3.Rz(30,'deg')*SO3.Rx(60,'deg')*SO3.Rz(45,'deg'))
sx=R1[0][0]
sy=R1[1][0]
sz=R1[2][0]

nx=R1[0][1]
ny=R1[1][1]
nz=R1[2][1]

ax=R1[0][2]
ay=R1[1][2]
az=R1[2][2]

phi1=np.arctan2(ax,-ay)
print(np.rad2deg(phi1))

phi2=np.arctan2(-ax,ay)
print(np.rad2deg(phi2))

theta1=np.arctan2(-ay*np.cos(phi1)+ax*np.sin(phi1),az)
print(np.rad2deg(theta1))

theta2=np.arctan2(-ay*np.cos(phi2)+ax*np.sin(phi2),az)
print(np.rad2deg(theta2))

psi1=np.arctan2(-nx*np.cos(phi1)-ny*np.sin(phi1),sx*np.cos(phi1)+sy*np.sin(phi1))
print(np.rad2deg(psi1))

psi2=np.arctan2(-nx*np.cos(phi2)-ny*np.sin(phi2),sx*np.cos(phi2)+sy*np.sin(phi2))
print(np.rad2deg(psi2))
