import numpy
def translationMatrix(tx=0, ty=0):
    return numpy.matrix([[1,0,tx],[0,1,ty],[0,0, 1]])
matrix=translationMatrix(1,1)
print("Translation Matrix : ")
print(matrix)

#Rotation Matrix

import numpy
def rotationMatrix(degree):
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[c, -s, 0],[s, c, 0],[0, 0, 1]])
matrix=rotationMatrix(30)
print("Rotation Matrix : ")
print(matrix)

#Scaling Matrix

import numpy
def scalingMatrix(sx=0, sy=0):
    return numpy.matrix([[sx,0,0],[0,sy,0],[0, 0,1]])
matrix=scalingMatrix(2,2)
print("Scaling Matrix : ")
print(matrix)
