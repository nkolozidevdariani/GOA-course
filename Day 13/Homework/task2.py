""" დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს და ბეჭდავს არის თუ არა ეს რიცხვი დადებითი, უარყოფითი ან ნულოვანი."""

num1 = int(input("please enter a number: "))

if num1 > 0:
    print("your number is positive")
elif num1 < 0:
    print("your number is negative")
else:
    print("your numbuer is zero")