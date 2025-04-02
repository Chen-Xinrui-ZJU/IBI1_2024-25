seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' #import sequence
import re #import re lib
longest=re.search(r'GT\S+AG',seq) #use search function to do greedy search on the sequence
print(longest[0],len(longest[0])) #print out result

#Pseudocode:
#import sequence and library
#use search function to do greedy search to find the longest intron
#print out the result and the length of it