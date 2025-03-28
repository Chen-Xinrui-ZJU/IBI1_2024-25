import numpy as np
import matplotlib.pyplot as plt #import necessary libs
population = np.zeros((100,100)) #generate a 100*100 array with 0 to form a square
outbreak = np.random.choice(range(100),2) #randomly choose a point in the square
population[outbreak[0],outbreak[1]] = 1 #as the outbreak of infection, give the point tag=1(infected)
beta=0.3
gamma=0.05
#define beta and gamma
plt.figure(figsize=(6,6))
plt.imshow(population, cmap='viridis')
plt.xticks([])
plt.yticks([])
plt.title("Time step 0")
plt.show()#When the time equals to 0, a graph can be directly generated without loops
for t in range(101):#required timestep is 100
    new_population=population.copy()
    infected = np.where(population==1) #to find all the infected points
    for i,j in zip(infected[0],infected[1]): #to zip all the xs and ys of infected points into two big lists (the zip code is the code that I have learnt outside of the course)
        if np.random.rand()<gamma:#a kind of draw, the principle of it is using a rand command to generate a float from 0 to 1 randomly and compare to the possibility provided to see the "draw result"
            new_population[i,j]=2 #they are recovered and given the tag=2(recovered)
        else:
            neighbours=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)] #all the possiblities arrays of the surronding 8 points of a point which array is (0,0)
            for x,y in neighbours:
                ni,nj=i+x,j+y #to have all the 8 surrounding ponts arrays of one given points
                if 0<=ni<100 and 0<=nj<100 and population[ni,nj]==0 and np.random.rand()<beta: #three conditions to be satisfied to become a infected point
                    new_population[ni,nj]=1
    population = new_population #update the population for next loop
    if t in [10,50,100]: #to print the graph of timesteps 10, 50, 100
        plt.figure(figsize=(6,6))
        plt.imshow(population, cmap='viridis')
        plt.xticks([])
        plt.yticks([])
        plt.title(f"Time step {t}")
        plt.show()

#Pseudocode:
#import all the libs and define all the intial variables and tags for 3 different categories(suspectible,infected,recovered)
#use commands given in the guidance to first generate a 100*100 square and give an outbreak of the infection
#for t in range(timesteps):
#   use where() to find all the infected points for further operations(infection and recovery)
#   generate long lists to store all the xs and ys of infected points
#       for those points that be recovered, transfer their tag from infected to recovered
#           for those points that are not recovered, they all have chance to infect their surrouding points
#           write command to represent all the surrounding points of a specific given point
#               for the neighbouring points which satisfies: 1.within the 100*100 square 2.tag is suspectible 3.beta , transfer their tags into infected
#   if t in (the four requested timestep points[0,10,50,100])
#       print the plots