print("Welcome to Simple Calculator : \n")
print("Press 1 for Summation\nPress 2 for Substraction\nPress 3 for Multiplication\nPress 4 for Division\nPress 5 for Modulas\n")
choice = int(input("Enter Your Choice : "))

if choice == 1:
    num1 = int(input("Enter Your First Number : "))
    num2 = int(input("Enter Your Second Number : "))
    print("The Summation is : ", num1 + num2)
elif choice == 2:
    num1 = int(input("Enter Your First Number : "))
    num2 = int(input("Enter Your Second Number : "))
    print("The Substraction is : ", num1 - num2)
elif choice == 3:
    num1 = int(input("Enter Your First Number : "))
    num2 = int(input("Enter Your Second Number : "))
    print("The Multiplication is : ", num1 * num2)
elif choice == 4:
    num1 = int(input("Enter Your First Number : "))
    num2 = int(input("Enter Your Second Number : "))
    print("The Division is : ", num1 / num2)
elif choice == 5:
    num1 = int(input("Enter Your First Number : "))
    num2 = int(input("Enter Your Second Number : "))
    print("The Modulas is : ", num1 % num2)
else:
    print("You Select a wrong Choice ")
    

