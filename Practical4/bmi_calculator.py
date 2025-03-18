#define two variables to store input weight and height
#do calculation following equation : (weight)/(height)**2
#use if-elif-else structure to put results into 3 categories
#print

weight = float(input('Please input your weight in kg:\t'))
height = float(input('Please input your height in m:\t'))
BMI=round(weight/height**2,2)
if BMI<18.5:
    print('your BMI is:',BMI,', you are underweight')
elif BMI>30:
    print('your BMI is:',BMI,', you are overweight')
else:
    print('your BMI is:',BMI,', you have normal weight')