uk_countries=[57.11,3.13,1.91,5.45]
cn_provinces=[65.77,41.88,45.28,61.27,85.15]
print(sorted(uk_countries))#sort and print
print(sorted(cn_provinces))#sort and print

import matplotlib.pyplot as plt 

labels1 = 'England','Wales','Northern Ireland','Scotland'
explode=(0,0,0.2,0) #to set the explode distance from center
plt.pie(uk_countries,explode=explode,labels=labels1,autopct='%1.1f%%',shadow=True,startangle=0) #form a pie chart
plt.axis('equal') #ensure it forms a whole pie
plt.show()#print the pie

labels2 = 'Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu'
explode=(0,0,0.2,0,0)
plt.pie(cn_provinces,explode=explode,labels=labels2,shadow=True,startangle=90)
plt.show() 