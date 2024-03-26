""" დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს და ბეჭდავს არის თუ არა ის ლუწი, კენტი თუ ნულის, გამოყენებით if, elif და სხვა."""

num = int(input("please enter a number: "))

if  num % 2 == 0:
    print("this number is even")
elif num % 2 == 1:
    print("this number is odd")