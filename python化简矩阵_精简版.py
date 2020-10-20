import numpy as np
def p(matrix):
    n=matrix.shape[0]
    for p in range(n):
        for i in range(p,n):
            if matrix[i][p]!=0:
                mother=-1/matrix[i][p]
                for j in range(i+1,n):
                    if matrix[j][p]!=0:
                        number=matrix[j][p]*mother
                        for k in range(p,n+1):
                            matrix[j][k]+= number*matrix[i][k]
                for k in range(0,n+1):
                    temp=matrix[p][k]
                    matrix[p][k]=matrix[i][k]
                    matrix[i][k]=temp
    for i in range(n):
        for j in range(i+1,n+1):
            matrix[i][j]/=matrix[i][i]
        matrix[i][i] =1
    for i in range(n-2,-1,-1):
        sums=0
        for j in range(i+1,n):
            sums+=matrix[i][j]*matrix[j][n]
            matrix[i][j]=0
        matrix[i][n]-=sums
    return matrix#numpy.array
