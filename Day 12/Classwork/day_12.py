# შექმენით პროგრამა, რომელიც ბეჭდავს 5-ის ჯერადებს 1-დან 50-ის ჩათვლით for loop-ის გამოყენებით.

# for i in range(1, 51):
#     if i % 5 == 0:
#         print(i)




# დაწერეთ პროგრამა, რომელიც ბეჭდავს ლუწ რიცხვებს 2-დან 20-ის ჩათვლით for loop-ის გამოყენებით.

# for i in range(2, 21):
#     if i % 2 == 0:
#         print(i)

# for i in range(2, 21, 2):
#     print(i)

# print(3%2)
# print(4%2)
# print(5%2)
# print(6%2)

# დაწერეთ ალგორითმი, რომელიც დაბეჭდავს 5-იდან ათის ჩათვლით რიცხვების ნამრავლს for loop-ის გამოყენებით.

# 1*
# 5*
# 6*
# 7*
# 8*
# 9*
# 10

# final_product = 1
# for i in range(5, 11):
#     final_product *= i
#     print("ამ ეტაპზე ნამრავლი უდრის: ", final_product, "ხოლო final product გავამრავლეთ ", i ,"ზე")



# დაწერეთ ალგორითმი, რომელიც მომხმარებელს შეეკითხება რიცხვს და თქვენ გამოიტანთ ამ რიცხვის ფაქტორიალს, შეასრულეთ for loop-ით.

# my_num = 5
# # 5-ისფაქტორიალი  ----  1*2*3*4*5 
# my_num = 7
# # 7-ისფაქტორიალი  ----  1*2*3*4*5*6*7 

# user_num = int(input("enter a number: "))
# final_product = 1
# for i in range(1, user_num + 1):
#     final_product *= i 

# print(user_num,"ის ფაქტორიალი არის:", final_product)



# დაწერეთ ალგორითმი, რომელიც მომხმარებელს შეეკითხება რიცხვს. თუ რიცხვი ლუწია გაყავით ორზე, სხვა შემთხვევაში გაამრავლეთ სამზე და მიუმატეთ ერთი.

# user_num = int(input("enter a number: "))
# if user_num % 2 == 0:
#     user_num /= 2 
#     print(user_num)
# else:
#     user_num = user_num * 3  + 1
#     print(user_num)


# while loop:

# დაიწყეთ 10-დან და დაითვალეთ 1-მდე, დაბეჭდეთ თითოეული რიცხვი.

# i = 10
# while i > 0:
#     print(i)
#     i -= 1




# განუწყვეტლივ სთხოვეთ მომხმარებელს მისი სახელი, სანამ არ შეიყვანს "quit"-ს.


# user_name = input("enter your name /or/ quit: ")
# i = 1 
# while user_name != "quit":
#     print("if you want to quit, type 'quit' in terminal, i said it", i, "times already")
#     user_name = input("enter your name /or/ quit: ")
#     i += 1
#     if i == 3:
#         print("metjer agar getyvi, sami kaci rom getyvis chainiki xaro, yurebidan ortqli unda gaushva")
    





# ამობეჭდეთ ყველა ლუწი რიცხვი 10-დან 20-მდე while ციკლის გამოყენებით.

# i = 10
# finish = 21
# while i < finish:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# მომხმარებელს შეაყვანინეთ რიცხვი და განაგრძეთ კითხვა მანამ, სანამ არ შეიტანს დადებით რიცხვს.

# user_num = int(input("enter a number: "))
# while user_num < 0:
#     user_num = int(input("enter a number: "))
# print("finally user input a positive number")



# 1-იდან 10-ის ჩათვლით არსებული ყველა რიცხვის კვადრატი გამოიტანეთ while ციკლის გამოყენებით.

i = 1
while i <= 10:
    print(i * i * i)
    # print(i ** 2) <---- მეორე გზა (ახარისხების)
    i += 1