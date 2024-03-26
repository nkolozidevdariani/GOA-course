"""მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი, საცხოვრებელი ადგილი და მეილი. ყველა შეინახეთ ცვლადებში და შემდეგ ჩაამატეთ სიაში, საბოლოოდ კი დაბეჭდეთ ეს სია."""

user_name = input("please enter a name: ")
user_lastname = input("please enter a lastname: ")
user_age = int(input("please enter your age: "))
user_location = input("please enter a your home location: ")
user_mail = input("please enter a your mail: ")

list = []
list.append(user_name)
list.append(user_lastname)
list.append(user_age)
list.append(user_location)
list.append(user_mail)

print(list)
