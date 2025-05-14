import re
import os
import sys
import pandas as pd
from Bio.Align import substitution_matrices
from Bio import pairwise2
#blosum62=substitution_matrices.load("BLOSUM62")
os.chdir("F:/^Course Material/IBI1/IBI1_2024-25/Practical13")
SOD2_h=open("human.fastq","r")
human=SOD2_h.read()
SOD2_m=open("mouse.fastq","r")
mouse=SOD2_m.read()
random_seq=open("random.fastq","r")
random=random_seq.read()
blosum62=pd.read_csv("blosum62.csv", index_col=0)

def sequence_extraction(a):
    sequence=re.findall(r'>.*?\n([A-Z\n]+)',a)
    text=sequence[0]
    return text.replace("\n","")
h_seq=sequence_extraction(human)
m_seq=sequence_extraction(mouse)
r_seq=sequence_extraction(random)
def alignment(seq1,seq2):
    blosum_score=0
    for a1,a2 in zip(seq1,seq2):
        score=blosum62.loc[a1,a2]
        blosum_score += score
    return blosum_score
print()
def similarity(seq1,seq2):
    identical_score=0
    for i in range(len(seq1)):
        if seq1[i]==seq2[i]:
            identical_score += 1
    similarity = round(identical_score/len(seq1)*100,2)
    return similarity
print(alignment(h_seq,m_seq),similarity(h_seq,m_seq))
print(alignment(h_seq,r_seq),similarity(h_seq,r_seq))
print(alignment(r_seq,m_seq),similarity(r_seq,m_seq))


"""Another method (using library)
def alignment(seq1,seq2):
    score = 0
    identical_count = 0
    for a1, a2 in zip(seq1, seq2):
        if (a1, a2) in blosum62:
            score += blosum62[(a1, a2)]
        elif (a2, a1) in blosum62:
            score += blosum62[(a2, a1)]
        if a1 == a2:
            identical_count += 1
    return identical_count
print(alignment(h_seq,m_seq))
"""
"""Hamming alignment test
def hamming_distance(seq1,seq2):
    edit_distance=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            edit_distance += 1
    return edit_distance
def similarity(seq1,seq2):
    similarity=round((1-(alignment(seq1,seq2)/len(seq1)))*100,2)
    return similarity
print("The score of Hamming distance is", hamming_distance(h_seq,m_seq),", with similarity(%) of", similarity(h_seq,m_seq))
print("The score of Hamming distance is", hamming_distance(h_seq,r_seq),", with similarity(%) of", similarity(h_seq,r_seq))
print("The score of Hamming distance is", hamming_distance(r_seq,m_seq),", with similarity(%) of", similarity(r_seq,m_seq))
"""
