import numpy

def translationMatrix(tx=0, ty=0, tz=0):
    return numpy.matrix([[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]])
matrix=translationMatrix(1,1,1)
print(matrix)

import numpy
def scalingMatrix(sx=0, sy=0, sz=0):
    return numpy.matrix([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0, 0,0,1]])
matrix=scalingMatrix(2,2,2)
print(matrix)


def rotationMatrix1(degree):
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[c, -s, 0, 0],[s, c, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
matrix=rotationMatrix1(30)
print(matrix)

def rotationMatrix2(degree):
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[1, 0, 0, 0],[0, c, -s, 0],[0, s, c, 0],[0, 0, 0, 1]])
matrix=rotationMatrix2(30)
print(matrix)

def rotationMatrix3(degree):
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[c, 0, s, 0],[0, 1, 0, 0],[-s, 0, c, 0],[0, 0, 0, 1]])
matrix=rotationMatrix3(30)
print(matrix)
