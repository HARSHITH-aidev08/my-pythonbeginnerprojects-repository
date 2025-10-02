opereator = input("Enter the opereator (+,-,*,/):")
num1 = float(input("Enter the number1:"))
num2 = float(input("Enter the number2:"))
if opereator == "+":
    result=num1+num2
    print(round(result,2))
elif opereator == "-":
    result=num1-num2
    print(round(result,2))
elif opereator == "*":
    result=num1*num2
    print(round(result,2))
elif opereator == "/":
    result=num1/num2
    print(round(result,2)) 
else:
    print(f"{opereator} is not a valid opereator")
