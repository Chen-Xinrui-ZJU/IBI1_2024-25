import re
def recognition():
    DNA_sequence=str(input("Please input your DNA sequence to be cut."))
    recognised_sequence=str(input('Please input restriction enzyme recognition sequence.'))
    if re.search(r"[^ACGT]+" , DNA_sequence) or re.search(r"[^ACGT]+" , recognised_sequence):
        print("Please check your input DNA sequence and restriction enzyme recognition sequence.") 
        return recognition()
    else:
        sequence_found=None
        for i in range(len(DNA_sequence)):
            splice=DNA_sequence[i:i+len(recognised_sequence)]
            if re.search(recognised_sequence,splice):
                print(f"The position of the input restriction enzyme is from {i+1} to {i+len(recognised_sequence)}.")
                sequence_found=splice
                break
        if sequence_found == None:
            print('Input restriction enzyme sequence not found.')
recognition()