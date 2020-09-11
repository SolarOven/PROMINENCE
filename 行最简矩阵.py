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
    matrix=matrix.astype("float")
    n=matrix.shape[0]
    for p in range(n):
        for i in range(p,n):
            if matrix[i][p]==0:
                pass
            else:
                #从第一个首位不为0的行开始
                mother=-1/matrix[i][p]#分母
                for j in range(i+1,n):
                    if matrix[j][p]==0:
                        pass
                    else:
                        number=matrix[j][p]*mother#分子*分母 组成倍数
                        print(number)
                        for k in range(p,n+1):
                            print(matrix[j][k]," + ",number," * ",matrix[i][k]," = ",end='')
                            matrix[j][k]+= number*matrix[i][k]
                            print(matrix[j][k],end="\n")
                for k in range(0,n+1):
                    temp=matrix[p][k]
                    matrix[p][k]=matrix[i][k]
                    matrix[i][k]=temp
                pass
    print(matrix)

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
    return matrix
