number1= int (input("enter the number: "))
number2= int (input("enter the number: "))
number3= int (input("enter the number: "))
if (number1>=number2)and(number1>=number3):
    largest = number1
elif (number2>=number1)and(number2>=number3):
    largest= number2
else:
    largest= number3

print("the largest number is:",largest)
