a = {'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}
print(a) #return dictionary

import numpy as np
import matplotlib.pyplot as plt

N=5 #Column numbers
percentage = (62.3,52.9,51,51,38.5) #Percentage of languages
ind = np.arange(N) #x locations for the groups
width = 0.35 #width of the bar
p1 = plt.bar(ind, percentage, width) #make a plot named p1, with x locations is ind, y locations is percentage and bar width is 0.35
plt.ylabel('Percentage')
plt.xlabel('Programming languages') #set x and y labels
plt.title('Programming language popularity')
plt.xticks(ind, ('JavaScript','HTML','Python','SQL','TypeScript')) #form a list of x ticks with labels
plt.yticks(np.arange(0,100,10)) #form a list of y ticks 
plt.show() #print plot p1

b = input('please input the language you are searching') 
if b in a: #to check if the language is in the dictionary
    print(a[b]) 
else:
    print('Language not found, please check the spelling of the language you are searching for.')
    
#Pseudocode:
#first create a dictionary and input the data of language and percentage in pairs, and write print() to return the dictionary
#To make barplot:
#first import numpy and matplotlib.pyplot
#set the column numbers, x locations for the bar, width for the bar
#create a list named precentage to store the y ticks of the data
#write a barplot creating command, set title, xticks, yticks and ylabels
#show the barplot

#write an if-else structure that:
#print the corresponding percentage if the input language can be found within the dictionary
#print "please check" message if the language can not be found