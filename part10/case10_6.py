while True:
    print("If you want to quit enter q")
    num1 = input("Please, enter the number ")
    num2 = input("Please, enter the number ")
    if num1 == 'q' or num2 == 'q':
        break
    try:
        summ = int(num1) + int(num2)
        print(summ)
    except ValueError:
        print("Please enter only number")
        
