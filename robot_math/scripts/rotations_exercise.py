from spatialmath import SO3

roty90=SO3.Ry(90, 'deg')
print(roty90)

rotx150 = SO3.Rx(150, 'deg')
print(rotx150)

bRc=roty90*rotx150
print(bRc)


rotx30 = SO3.Rx(30,'deg')
print(rotx30)