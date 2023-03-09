from spatialmath import *
import matplotlib.pyplot as plt
import sympy as sym
import numpy as np
from numpy.linalg import det
from numpy.linalg import inv

Q1, c1, c2,  = sym.symbols('Q1 c1 c2') #Create some symbolic variables
Q2, c3, c4,  = sym.symbols('Q2 c3 c4')

T01 = SE3.Rz(Q1)*SE3(0,0,c1)*SE3(c2,0,0)*SE3.Rx(90, 'deg')
T01.print()


T12 = SE3.Rz(Q2)*SE3(0,0,c3)*SE3(c4,0,0)*SE3.Rx(0, 'deg')
T12.print()

T02=T01*T12
T02.print()

#Consider all c1, c2, c3, c4 as 1, Q1 =Q2 =0
T01 = SE3.Rz(0)*SE3(0,0,1)*SE3(1,0,0)*SE3.Rx(90, 'deg')
T01.print()


T12 = SE3.Rz(0)*SE3(0,0,1)*SE3(1,0,0)*SE3.Rx(0, 'deg')
T12.print()

T02=T01*T12
T02.print()

T0=SE3(0,0,0)
T0.plot(frame='0',color='red')
T01.plot(frame='1',color='green')
T02.plot(frame='2',color='blue')
plt.show()



#Consider all c1, c2, c3, c4 as 1, Q1 = 0 Q2 =90
T01 = SE3.Rz(0)*SE3(0,0,1)*SE3(1,0,0)*SE3.Rx(90, 'deg')
T01.print()


T12 = SE3.Rz(90,'deg')*SE3(0,0,1)*SE3(1,0,0)*SE3.Rx(0, 'deg')
T12.print()

T02=T01*T12
T02.print()

T0=SE3(0,0,0)

T0.plot(frame='0',color='red')
T01.plot(frame='1',color='green')
T02.plot(frame='2',color='blue')
plt.show()