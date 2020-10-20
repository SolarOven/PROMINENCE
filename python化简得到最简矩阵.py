import numpy as np
def p(matrix):
    '''
    numpy arry
    matrix:
        [
            [arg,arg,arg,arg],
            [arg,arg,arg,arg],
            [arg,arg,arg,arg]        
        ]
        
    需要numpy库
    requires numpy
    '''
    #生成阶梯阵
    
    n=matrix.shape[0]#获取行数
    for p in range(n):#分别查找最终位于0~n行的行
        
        for i in range(p,n):#当前查找：“最终位于第p行”的行，从第p行向下查找，即令i~[p,n]
            if matrix[i][p]==0:#若第i行的第p位=0，说明不是所需要的行
                pass
            else:#开始高斯消元法
                
                mother=-1/matrix[i][p]#分母
                for j in range(i+1,n):#从找到的第一个符合“第p位！=0”的行向下查找以求相减消元
                    if matrix[j][p]==0:
                        pass
                    else:
                        number=matrix[j][p]*mother#分子*分母 组成倍数，该倍数+第i行的第p位=0，从而消元
                        print(number)
                        for k in range(p,n+1):
                            print(matrix[j][k]," + ",number," * ",matrix[i][k]," = ",end='')
                            matrix[j][k]+= number*matrix[i][k]
                            print(matrix[j][k],end="\n")
                #将查找到的“最终位于第p行的行”置于第p行(当前为第i行)
                for k in range(0,n+1):
                    temp=matrix[p][k]
                    matrix[p][k]=matrix[i][k]
                    matrix[i][k]=temp
    print(matrix)
    #化为那啥，忘了叫啥了，反正是：
    '''
        [
            [1,0,0,x1],
            [0,1,0,x2],
            [0,0,1,x3]        
        ]
    '''#这种形式
    
    #将首元化为1
    for i in range(n):
        for j in range(i+1,n+1):
            matrix[i][j]/=matrix[i][i]
        matrix[i][i] =1
    #由下向上代入，以令除首元外的矩阵的位置为0
    for i in range(n-2,-1,-1):
        sums=0
        for j in range(i+1,n):
            sums+=matrix[i][j]*matrix[j][n]
            matrix[i][j]=0
        matrix[i][n]-=sums
        
    return matrix#numpy.array
