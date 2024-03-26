"""დაწერეთ ალგორითმი, რომელიც მომხმარებელს შეეკითხება რიცხვს და თქვენ გამოიტანთ ამ რიცხვის ფაქტორიალს, შეასრულეთ for loop-ით."""

num = int(input("please enter a number: "))
product = 1

for i in range(1,num + 1):
    product = product * i
print(product)
