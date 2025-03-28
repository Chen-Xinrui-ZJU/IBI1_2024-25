import numpy as np
import matplotlib.pyplot as plt
S = 9999
I = 1
R = 0
N = S+I+R
beta = 0.3
gamma = 0.05
#define beta and gamma
s = [S]
i = [I]
r = [R]
#create lists for plotting and saving result from following commands
for j in range(0,1000):
    S_current = s[-1]
    I_current = i[-1]
    R_current = r[-1]
    new_i = int(np.sum(np.random.choice([0,1],S_current,p=[1-beta*I_current/N,beta*I_current/N]))) #calculate the infected number that increase in a new loop
    new_r = int(np.sum(np.random.choice([0,1],I_current,p=[1-gamma,gamma])))   #calculate the recovery number that increase in a new loop 
    s.append(S_current-new_i) #for the new susceptible number after one loop, it can be calculated by the susceptible number from last loop minus the infected number that increase in the loop
    i.append(I_current+new_i-new_r) #for the new infected number, it can be calculated by adding new_i and substracting new_r from the last infected number
    r.append(R_current+new_r) #for the new recovery number after one loop, it's simply a kind of accumulation, which is calculated by simply adding the new recovery number in this loop to the older accumulated number
plt.plot(s,label='Susceptible')
plt.plot(i,label='Infected')
plt.plot(r,label='Recovered')
#generate three curves using the three lists respectively
plt.xlabel('Time step')
plt.ylabel('Number of people')
plt.title('SIR Model')
#titling
plt.legend()
plt.show()

#Pseudocode:
#import neccesary libraries
#define the numbers of people of the susceptible, infected and recovered, together with gamma and beta
#create lists for plotting and data storing
#for j in timestep(1000)
#   define variables that can pick out the last data in the lists
#   to calculate newi and newr, use the np.random.choice command. If one is infected, add 1 to the sum, if one is not infected then add 0. Then transform the sum into integer for following steps
#   calculate the new numbers of people for each categories and add then to the end of lists respectively
#   loop ends
#print the plot and show
