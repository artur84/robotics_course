#!/usr/bin/env python
from spatialmath import SO3
import spatialmath.base as tr 
import sympy as sym
import numpy as np
from numpy.linalg import det
from numpy.linalg import inv

Q, B, a = sym.symbols('Q B a') #Create some symbolic variables

#Create a rotation matrix about x
Rotx=SO3.Rx(Q) #High level structure
#rotx=tr.rotx(Q) #Low level structure (numpy array)
print("Rx")
print(Rotx)
#print(rotx)

#Create a rotation matrix about y
Rotx=SO3.Rx(Q) #High level structure
#rotx=tr.rotx(Q) #Low level structure (numpy array)
print("Rx")
print(Rotx)
#print(rotx)

#Create a rotation matrix argument in radians
R_pi = SO3.Rx(np.pi)
R_pi.print()

#Create a rotation matrix in degrees
R_30 = SO3.Rx(30,'deg')
R_30.print()

R_minus30 = SO3.Rx(-30, 'deg')
R_minus30.print()

# Inverse of a rotation matrix 
R30_inv=R_30.inv()
print("inverse of Rx")

print(R30_inv)

# Determinant of a rotation matrix (using numpy.linalg.det function)
det(R_30)

#Rotation about y-axis
Ry=SO3.Ry(B)
print("Ry")
print(Ry)


# Rotation about z-axis
#Rz=tr.rotz(a)
Rz=SO3.Rz(a)
print("Rz")
print(Rz)

detx = Rotx_inv.norm()
print("R")
print(R)

#print("simplify R")
#print(sym.simplify(R))


