
import numpy as np

matrix = np.ones(shape = (25,25))

for i in range(5,20,1):
    matrix[:5,i] = range(6,1,-1)
    matrix[20:25,i]=range(2,7,1)

    matrix[i,:5] = range(6,1,-1)
    matrix[i,20:25]=range(2,7,1)

for i in range(0,5):
    for j in range(0,5):
        if i <= j:
            matrix [i,j]=6-i
            matrix [i,-(j+1)]= 6-i
            matrix[-(i+1),j]=6-i
            matrix[-(i+1),-(j+1)]=6-i
        if i > j:
            matrix [i,j]=6-j
            matrix [i,-(j+1)]= 6-j
            matrix[-(i+1),j]=6-j
            matrix[-(i+1),-(j+1)]=6-j



print matrix




"""
n=25
x,y=np.meshgrid(range(0,25,1),range(0,25,1))

#print x,y
matrix = np.round(((1+(24+1)/(25-1)*np.sqrt(2*((x-(25+1)/2)**2+(y-(25+1)/2)**2)))),0)
matrix = matrix - 17
print matrix.shape

print matrix

for i in range(5,21,1):
    for j in range(5,21,1):
        matrix[i,j]=1



for i in range(5,20,1):
    matrix[:5,i] = range(6,1,-1)
    matrix[20:26,i]=range(2,7,1)

    matrix[i,:5] = range(6,1,-1)
    matrix[i,20:26]=range(2,7,1)

#print matrix
"""
