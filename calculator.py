print("mini calculator")
num1 = float(input("enter the fist number: "))
num2 = float(input("enter the second number: "))
print (''' press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division2 
       \npress 5 for exponential \npress 6 for square root''')

choice = int(input("enter your choice from 1-6: "))
if choice ==1:
    print (num1 + num2)
elif choice ==2:
    print (num1 - num2)
elif choice ==3:
    print (num1 * num2)
elif choice ==4:
    print (num1 / num2)
elif choice ==5:
    print(num1 ** num2)
elif choice == 6:
    print(num1 **(1/2))
else:
    print("invalid input")