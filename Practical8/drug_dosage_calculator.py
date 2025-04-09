def dosage_calculator():
    weight = int(input('Please input your weight:'))
    strength = int(input('Please input the strength of paracetamol in mg/5ml:'))
    if 10>weight or weight>100:
        print('Please input correct weight')
        return dosage_calculator()
    elif strength not in [24,50]:
        print('Please input correct strength')       
        return dosage_calculator()
    else:
        volumn = 15*weight/strength*5
        return(volumn)
result=dosage_calculator()
print(result)