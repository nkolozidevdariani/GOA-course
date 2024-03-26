"""მომხმარებელს შეაყვანინეთ რიცხვი და განაგრძეთ კითხვა მანამ, სანამ არ შეიტანს დადებით რიცხვს."""

num = int(input("please enter a number: "))
while num <= 0:
    num = int(input("please enter a number: "))