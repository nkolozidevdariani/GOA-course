"""შექმენით კალკულატორი, სადაც მომხმარებელი აირჩევს შემდეგ ოპერაციებს: + - * / და მის მიერ შემოტანილი ორი რიცხვით მიიღებს პასუხს."""

operation = input("please enter {+,-,*,/}: ")
num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number: "))

if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2)

else:
    print("error")
