"""მომხმარებელს ჯერ შემოატანინეთ ბიუჯეტი, შემდეგ კი ის თანხა, რომელიც სასურველი ნივთის საყიდლად სჭირდება. დაბეჭდეთ შეუძლია ყიდვა თუ არა."""

buget = int(input("please enter your buget: "))

if buget >= 30:                 #thing costs 30
    print("you can buy thing")
else:
    print("you can't buy thing")