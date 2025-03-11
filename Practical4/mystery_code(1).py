# What does this piece of code do?
# Answer: It's a command to show how many times the two random command take to generate the same integer

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress>=0:
	progress+=1 #every time the two random number is not equal, the progress add 1 to itself
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n: #judge whether the two random command have generated the same integer
		print(progress)
		break #if so print progress and jump out of the loop to finish the whole process

