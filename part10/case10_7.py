num1 = input("Please, enter the number ")
num2 = input("Please, enter the number ")
try:
    summ = int(num1) + int(num2)
    print(summ)
except ValueError:
    print("Please enter only number")
    
