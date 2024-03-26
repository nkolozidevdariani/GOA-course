"""მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ თუ არის როგორც ორის, ასევე სამის ჯერადი.
არსებობის შემთხვევაში დაპრინტეთ ეს რიცხვი, ხოლო თუ არ იქნება მაშინ თავიდან შეეკითხეთ (გამოიყენეთ while ციკლი)."""

num = int(input("please enter a number: "))
while True:
    if num % 2 == 0 and num % 3 == 0:
        print(num)
        break
    else:
        num = int(input("please enter a number: "))