import numpy as np
import pandas as pd
data ={'a':0.,'b':1.,'c':2.}
s=pd.Series(data)
print(s)
 data= {'Name':['Tom','jack','steve','ricky'],'Age':[28,49,1,67]}
df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(df)
a= np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
print(a[0,1])
import matplotlib.pyplot as plt
x=[2,5,6,8]
y=[1,4,6,1]
plt.plot(x,y)
plt.title('Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
plt.bar([1,2,3],[20,40,30],label="Bmw",width=.5)
plt.bar([5,7,8],[12,76,34],label='Audi', color='y', width=.5)
plt.legend()
plt.xlabel('d')
plt.ylabel('c')
plt.title('ds')
plt.show()

