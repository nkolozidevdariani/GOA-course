s1 = int(input("please eneter first side: "))
s2 = int(input("please eneter second side: "))
s3 = int(input("please eneter third side: "))


is_valid = (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)

while is_valid != True:
    s1 = int(input("please eneter first side: "))
    s2 = int(input("please eneter second side: "))
    s3 = int(input("please eneter third side: "))

    is_valid = s1 + s2 > s3

