"""მომხმარებელს შეეკითხეთ ასაკი. შექმენით ცვლადი, სადაც შენახული იქნება 10 წლის შემდეგ მომხმარებლის ასაკი. 
საბოლოოდ დაპრინტეთ მომხმარებლის ასაკსა და 10 წლის შემდეგ წლოვანებას შორის არსებული მთელი რიცხვები. """

age = int(input("please enter your age: "))
new_age = age + 10

for i in range(age,new_age):
    print(i)
