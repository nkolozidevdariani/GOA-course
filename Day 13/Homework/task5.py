""" დაწერეთ პროგრამა, რომელიც ბეჭდავს კვირის დღეს მომხმარებლის მიერ შეყვანილი რიცხვის საფუძველზე 
(1 ორშაბათისთვის, 2 სამშაბათისთვის და ა.შ.) if, elif და სხვა გამოყენებით. USE IF-ELIF-ELSE"""

num = int(input("please enter a number: "))

if num == 1:
    print("monday")
elif num == 2:
    print("tuesday")
elif num == 3:
    print("wednesday")
elif num == 4:
    print("thursday")
elif num == 5:
    print("friday")
elif num == 6:
    print("saturday")
elif num == 7:
    print("sunday")
else:
    print("ERROR")
