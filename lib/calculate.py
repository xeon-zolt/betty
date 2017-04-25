def calculate(num1,num2,operator):
    if(operator == "+"):
        print(num1+num2)
    elif(operator == "-"):
        print(num1-num2)
    elif(operator == "*"):
        print(num1*num2)
    elif(operator == "/"):
        if(num2==0):
            print("Cant divide by Zero")
        else:
            print(num1/num2)
    else:
        print("Oops Error calculating")
