uk_countries=[57.11,3.13,1.91,5.45]
cn_provinces=[65.77,41.88,45.28,61.27,85.15]
print(sorted(uk_countries))#sort and print
print(sorted(cn_provinces))#sort and print

import matplotlib.pyplot as plt 

labels1 = 'England','Wales','Northern Ireland','Scotland'
#to set the explode distance from center
plt.pie(uk_countries,labels=labels1,autopct='%1.1f%%',shadow=True,startangle=0) #form a pie chart
plt.axis('equal') #ensure it forms a whole pie
plt.show()#print the pie

labels2 = 'Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu'
explode=(0.2,0,0,0,0) #to set the explode distance from center
plt.pie(cn_provinces,explode=explode,labels=labels2,shadow=True,startangle=90)
plt.show() 

#Pseudocode:
#create 2 lists to store the population data respectively
#sort the lists then print them

#To draw pie charts:
#import matplotlib first
#name two pie charts and set them with labels, datasource(the two lists created beforehand), explode or not, the data display form etc.)
#print the pie