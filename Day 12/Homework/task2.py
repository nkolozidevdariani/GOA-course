"""შექმენით ცვლადი, სადაც შეინახავთ თქვენთვის სასურველ პაროლს. მომხმარებელს შეეკითხეთ პაროლი და სანამ სწორს არ შემოიტანს თავიდან შეეკითხეთ, 
თან დაუმატეთ თუ მერამდენე ცდაზეა (გამოიყენეთ while ციკლი). თუ მან მეხუთე ცდაზეც ვერ შეიყვანა სწორად, დაუპრინტეთ, რომ სისტემა დაბლოკილია."""

password = "nika2009"

user_password = input("please enter a password: ")

guesess = 1
while user_password != password:
    user_password = input("please enter a password: ")
    guesess = guesess + 1
    print("guesess",guesess)
    if guesess > 5:
        print("system blocked")
        break