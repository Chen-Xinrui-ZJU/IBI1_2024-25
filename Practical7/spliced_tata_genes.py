import sys
import re
database = open(r'F:\^Course Material\IBI1\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
text=database.read()
all = re.findall(r'>.*?gene:(\S+).*?\n([A-Z\n]+)',text)
DA = str(input('Please enter the splice donor/acceptor combinations： ')) 
donor=''
acceptor=''
if DA == 'GTAG':
    donor = 'GT'
    acceptor = 'AG'
    newfile=open(r'F:\^Course Material\IBI1\IBI1_2024-25\Practical7\GTAG_spliced_genes.fa','w')
elif DA == 'GCAG':
    donor = 'GC'
    acceptor = 'AG'
    newfile=open(r'F:\^Course Material\IBI1\IBI1_2024-25\Practical7\GCAG_spliced_genes.fa','w')
elif DA == 'ATAC': 
    donor = 'AT'
    acceptor = 'AC'
    newfile=open(r'F:\^Course Material\IBI1\IBI1_2024-25\Practical7\ATAC_spliced_genes.fa','w')
else:
    print('Please enter the correct splice donor/acceptor combinations')
for gene,sequence in all:
    sequence_text=sequence.replace('\n','').upper()
    splice=re.findall((f'{donor}'+r'[A-Z]*?'+f'{acceptor}'),sequence_text)          
    for splice_sequence in splice:
        if re.findall(r'TATA[AT]A[AT]', splice_sequence):
            number=len(re.findall(r'TATA[AT]A[AT]', splice_sequence))
            newfile.write(f'>{gene}\t{number}\n{splice_sequence}\n')
newfile.close()
database.close()

#Pseudocode:
#Import libraries
#Open the input file and read its content
#Set a variable to store the gene and sequence pair
#Create a new file to store the output
#Ask the user to input the splice donor/acceptor combinations
#Set the donor and acceptor variables
#If the user input is 'GTAG', 'GCAG' or 'ATAC', create a new file to store the output based on the donor/acceptor combinations
    #Create a new file to store the output based on the donor/acceptor combinations
#Else, print an error message
#Use a for-loop to iterate all the gene and sequence pairs
    #Replace all the \n to make the sequence continuous (very important, otherwise some sequences will be missed)
    #Write a command to find the splice donor/acceptor combinations in the sequence
    #If the splice donor/acceptor combinations are found in the sequence_text
        #Write the gene and sequence to the new file
#Close the new file and the input file
