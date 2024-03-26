"""მომხმარებელს შემოატანინეთ სამკუთხედის სამი გვერდი და შეამოწმეთ თუ არსებობს ის. არსებობის შემთხვევაში დაპრინტეთ, რომ მონაცემები სწორია, 
სხვა შემთხვევაში შემოატანინეთ გვერდების მნიშვნელობები თავიდან ( გამოიყენეთ while ციკლი )."""


a = int(input("Enter first s: "))
b = int(input("Enter second s: "))
c = int(input("Enter third s: "))

while True:
    if a + b >= c and a + c >= b and b + c >= a:
        print("Your triangle exists")
        break
    print("Your triangle doesn't exist")
    a = int(input("Enter first s: "))
    b = int(input("Enter second s: "))
    c = int(input("Enter third s: "))
