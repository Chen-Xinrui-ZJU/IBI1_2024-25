
#pseudocode:
#Define a variable that equals to 0
#T(i+1) = T(i) + i (i should start with 0)
#print command should be written within the loop


T=0
for i in range(1,11): #The triangle sequence can be reached via continuous adding, so it requires for-loop
    T = T+i
    print(T)
