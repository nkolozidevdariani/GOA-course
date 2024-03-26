opearation = input(" please enter operation (+,-,*,/): ")
num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number: "))

if opearation == '+':
    print(num1 + num2)
elif opearation =='-':
    print(num1 - num2)
elif opearation =='*':
    print(num1 * num2)
elif opearation == '/':
    print(num1 / num2)
else:
    print("operation is not vaild")