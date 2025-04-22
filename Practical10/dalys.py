import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("F:/^Course Material/IBI1/IBI1_2024-25/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#print(dalys_data.describe())
#print(dalys_data.iloc[0:10,2]) #1999 was the 10th year for which DALYs were recorded in Afghanistan

yrs=dalys_data.iloc[:,2]
my_row=[]
for yr in yrs:
    if yr==1990:
        my_row.append(True)
    else:
        my_row.append(False)
#print(dalys_data.iloc[my_row,:])

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
fr = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]]
print(uk.describe())
print(fr.describe())
#the mean DALYs for the UK is larger than France

plt.plot(uk.Year, uk.DALYs, 'g.') # + * . o all work!

plt.title("DALYs in the UK")
plt.xlabel("Years")
plt.ylabel("DALYs")
plt.xticks(uk.Year,rotation=-45) #rotate the xlabels to makes the plot more compacted in x axis
plt.show()


cn = dalys_data.loc[dalys_data.Entity=="China", ["DALYs", "Year"]]
plt.plot(cn.Year, cn.DALYs, 'r.', label="China")
plt.plot(uk.Year, uk.DALYs, 'g.', label="the UK") # + * . o all work!
plt.title("DALYs in the UK and China")
plt.xlabel("Years")
plt.ylabel("DALYs")
plt.legend()
plt.xticks(uk.Year,rotation=-45) #rotate the xlabels to makes the plot more compacted in x axis
plt.show()