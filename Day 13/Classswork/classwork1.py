registarad_passsword = "nika2009"

password = input("please enter your password: ")

while password != registarad_passsword:
    password = input("please enter you password: ")
    if password == registarad_passsword:
        print("you have accses an your account")
    else:
        print("you have entered wrong password, please try again")