def p(matrix):
    '''
    numpy arry
    matrix:
        [
            [arg,arg,arg,arg],
            [arg,arg,arg,arg],
            [arg,arg,arg,arg]        
        ]
    '''
    n=matrix.shape[0]
    for p in range(n):
        for i in range(p,n):
            if matrix[i][p]==0:
                pass
            else:
                mother=-1/matrix[i][p]#分母
                for j in range(i+1,n):
                    if matrix[j][p]==0:
                        pass
                    else:
                        number=matrix[j][p]*mother#分子*分母
                        print(number)
                        for k in range(p,n+1):
                            print(matrix[j][k]," *",number," + ",matrix[i][k]," = ",end='')
                            matrix[j][k]+= number*matrix[i][k]
                            print(matrix[j][k],end="\n")
                for k in range(0,n+1):
                    temp=matrix[p][k]
                    matrix[p][k]=matrix[i][k]
                    matrix[i][k]=temp
                pass
    return matrix
