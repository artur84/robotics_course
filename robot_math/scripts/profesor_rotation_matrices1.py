#!/usr/bin/env python
from spatialmath import *
import spatialmath.base as tr 
import sympy as sym
Q, B, a = sym.symbols('Q B a')

Rx=tr.rotx(Q)
#Rx=SO3.Rx(Q)
print(Rx)

Ry=tr.roty(B)
#Ry=SO3.Ry(B)
print("Ry")
print(Ry)

Rz=tr.rotz(a)
#Rz=SO3.Rz(a)
print("Rz")
print(Rz)

R=Rx@Ry@Rz
print("R")
print(R)

#print("simplify R")
#print(sym.simplify(R))


