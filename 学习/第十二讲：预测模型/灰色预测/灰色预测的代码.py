import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


# #将xlsx文件进行转换变成csv文件
# excel_file='daima.xlsx'
# df=pd.read_excel(excel_file)#读取Excel文件

# csv_file='daima.csv'#指定CSV文件路径
# df.to_csv(csv_file,index=False)#index=False，表示不保存索引序列

#读取csv文件
'''
df=pd.read_csv('daima.csv',encoding='utf-8')
print(df.head(3))#打印daima.csv文件的前3行
'''

#画图前的准备
plt.rcParams['font.sans-serif'] = ['SimSun'] #设置字体为宋体
#画出时间序列图，大致了解数据趋势
df=pd.read_csv('daima.csv',encoding='utf-8')#导入CSV文件
plt.figure(figsize=(12,6))#图的窗口大小
plt.plot(df['year'],df['zong'],label='时间序列数据',color='blue')
#创建一个二维图表，第一个"date"作为x轴，第二个“Value”作为y轴，图例标签为“时间序列数据”，颜色为蓝色
plt.xlabel('时间')
plt.ylabel('值')
plt.title('时间序列图')
plt.legend()
plt.grid(True)
plt.show()#显示图像

#数据导入
date_zong=[]
zong=df['zong']
for i in zong:
    date_zong.append(i)
n=len(date_zong)
X0=np.array(date_zong)

#累加生成
zong_data_agg = [sum(date_zong[0:i+1]) for i in range(n)]
X1 = np.array(zong_data_agg)#累加x1

#计算数据矩阵B和数据向量Y
B = np.zeros([n-1,2])
Y = np.zeros([n-1,1])
for i in range(0,n-1):
    B[i][0] = -0.5*(X1[i] + X1[i+1])
    B[i][1] = 1
    Y[i][0] = X0[i+1]

#计算GM(1,1)微分方程的参数a和u
#A = np.zeros([2,1])
A = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)
a = A[0][0]
u = A[1][0]

#建立灰色预测模型
XX0 = np.zeros(n)
XX0[0] = X0[0]
for i in range(1,n):
    XX0[i] = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(i));

#模型精度的后验差检验
e = 0      #求残差平均值
for i in range(0,n):
    e += (X0[i] - XX0[i])
e /= n
print("残差平均值：",e)

#求历史数据平均值
aver = 0;     
for i in range(0,n):
    aver += X0[i]
aver /= n
print("历史数据平均值：",aver)

#求历史数据方差
s12 = 0;     
for i in range(0,n):
    s12 += (X0[i]-aver)**2;
s12 /= n
print('历史数据方差：',s12)

#求残差方差
s22 = 0;       
for i in range(0,n):
    s22 += ((X0[i] - XX0[i]) - e)**2;
s22 /= n
print('残差方差：',s22)

#求后验差比值
C = s22 / s12   
print('差比值：',C)

#求小误差概率
cout = 0
for i in range(0,n):
    if abs((X0[i] - XX0[i]) - e) < 0.6754*math.sqrt(s12):
        cout = cout+1
    else:
        cout = cout3
        
P = cout / n
print('小误差概率：',cout)

if (C < 0.35 and P > 0.95):
    #预测精度为一级
    m=int(input("需要预测的年数："))   #请输入需要预测的年数
    print('往后m各年负荷为：')
    f = np.zeros(m)
    for i in range(0,m):
        f[i] = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(i+n))
        print(f[i])    
else:
    print('灰色预测法不适用')


