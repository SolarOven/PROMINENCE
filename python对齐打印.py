__author__="SolarOven"
__version__=2.1

'''
用法：
puu(x),x是字符串,或者是一组用逗号隔开的变量
boo(),把刚才你所有puu的x全部输出，上下对齐。

usage：
puu(x),x is a string separated by spaces,or a group of variables separated with ','
boo(),printf what you just puu all. up and down the aligenment

例如：
for example:

    n='xxx'
    s='?'
    a='11'
    puu("name sex age")
    puu(n,s,a)
    boo()
    >>
        name sex age
        xxx  ?   11

差不多就是这样。。
almost like that..
'''


#简称解释：比如“sss kkk”其中，sss就是一个需对齐元素，一下简称齐素
n=-1#n为索引而非序列
z=[]#数组型不用global也能在函数中修改
    #z=[行[齐素     ]]
l={} #l记录此列需要多宽
s_l={} #记录每个齐素的长度

def disolve(a):
    global n
    n+=1
    z.append([])
    s_len=0#记录每个齐素的长度
    ali_elems=0#每行中齐素的个数 记录在l中，是索引而非序列
    
    elem=''#将字符组合成齐素
    for i in enumerate(a):
        if i[1]==' ':
            try:
                l[ali_elems]=max(l[ali_elems],s_len)
            except:
                l[ali_elems]=max(0,s_len)
            #                   记录l
            z[n].append(elem)#  记录齐素内容
            s_l[elem]=s_len#    记录齐素长

            ali_elems+=1#       齐素索引递增
            elem=''#            重置齐素内容
            s_len=0#            重置齐素长
        elif i[0]==len(a)-1:
            elem+=i[1]#         将此字符记录在elem
            s_l[elem]=s_len#    记录齐素长
            z[n].append(elem)#  记录齐素内容
            try:
                l[ali_elems]=max(l[ali_elems],s_len)
            except:
                l[ali_elems]=max(0,s_len)
            #                   记录l
            ali_elems+=1#       齐素索引递增
            elem=''#            重置齐素内容
            s_len=0#            重置齐素长
        elif 0x4E00<ord(i[1])<0x9FA5:#是否是常用汉字
            s_len+=2
            elem+=i[1]
        else:
            s_len+=1
            elem+=i[1]

def boo(x=' '):
    for h in z:
        for elem in enumerate(h):
            print(elem[1],end=(x+' '*(l[elem[0]]-s_l[elem[1]])))
        print('')

def puu(*a):
        if len(a)==1 and isinstance(a[0],str):
            disolve(a[0])
        else:
        
            h=''
            for i in a:
                w=str(i)

                if ' ' in w:
                    w=w.replace(' ','')
                h+=(w+' ')
            disolve(h)
