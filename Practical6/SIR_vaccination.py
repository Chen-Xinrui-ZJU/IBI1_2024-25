import numpy as np
import matplotlib.pyplot as plt
N = 10000
I = 1
R = 0
beta = 0.3
gamma = 0.05
#define beta and gamma all the initial values
for k in range(11): 
    percentage = k*10 #generate a list of percentage
    V = int(N*k/10) #calculate the vaccinated number
    S = N-I-R-V
    s = [S]
    i = [I]
    r = [R]
    if k <10:#here the if-structure is designed to avoid the line22 to get the negative result when k=10
        for j in range(0,1000):
            S_current = s[-1]
            I_current = i[-1]
            R_current = r[-1]
            new_i = int(np.sum(np.random.choice([0,1],S_current,p=[1-beta*I_current/N,beta*I_current/N]))) 
            new_r = int(np.sum(np.random.choice([0,1],I_current,p=[1-gamma,gamma])))    
            s.append(S_current-new_i)
            i.append(I_current+new_i-new_r)
            r.append(R_current+new_r+V) 
    else:
        i=[]
        for k in range(0,1000):
            i.append(0) #when k=10, which means that everyone is vaccinated, then the infected number should be 0 all the time,so just generate a list with a thousand 0
            
    plt.plot(i,label=str(percentage)+'%') #generate labels from 0% to 100%
plt.xlabel('Time step')
plt.ylabel('Number of people')
plt.title('SIR Model')
plt.legend()
plt.show()

#Pseudocode:
#import necessary libs and define intial variables
#use a for-loop to run the command when the vaccinated rate is 0%, 10%, ... , 100%
#for j in timestep(1000)
#   define variables that can pick out the last data in the lists
#   to calculate newi and newr, use the np.random.choice command. If one is infected, add 1 to the sum, if one is not infected then add 0. Then transform the sum into integer for following steps
#   calculate the new numbers of people for each categories and add then to the end of lists respectively
#   loop ends
#put all the infected lists from each vaccinated rate together to form a plot with 11 curves