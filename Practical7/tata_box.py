import sys
import re
input = open(r'F:\^Course Material\IBI1\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
text=input.read()
all = re.findall(r'>.*?gene:(\S+).*?\n([A-Z\n]+)',text) #to find gene names after "gene:" and the sequence after "\n", and find gene sequence on the next line of gene name and before ">"
newfile=open(r'F:\^Course Material\IBI1\IBI1_2024-25\Practical7\tata_genes.fa','w')
sequence_text = ''
for gene,sequence in all:
    sequence_text=sequence.replace('\n','')   #use '' to replace new line markers
    tata = re.findall(r'TATA[AT]A[AT]',sequence_text) #use [AT] to match A or T
    if tata:
        newfile.write(f'>' + gene + '\n' + sequence)

#Pseudocode:
#import libraries
#open the input file and read its content
#set a variable to store the gene and sequence pair
#create a new file to store the output
#use a for-loop to iterate all the gene and sequence pairs
    #replace all the \n to make the sequence continuous (very important, otherwise some sequences will be missed)
    #write a command to find the TATA box in the sequence
    #if tata is found in the sequence_text
        #write the gene and sequence to the new file