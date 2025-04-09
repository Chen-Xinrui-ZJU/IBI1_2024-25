import re
def recognition():
    DNA_sequence=str(input("Please input your DNA sequence to be cut."))
    recognised_sequence=str(input('Please input restriction enzyme recognition sequence.'))
    if re.search(r"[^ACGT]+" , DNA_sequence) or re.search(r"[^ACGT]+" , recognised_sequence):
        print("Please check your input DNA sequence and restriction enzyme recognition sequence.") 
        return recognition()
    else:
        print(re.search(recognised_sequence,DNA_sequence))
recognition()