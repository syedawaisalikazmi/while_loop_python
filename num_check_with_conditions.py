num=int(input("enter a num from 1 to 10: "))

while num<1 or num>10:
    print(f"the {num} is not valid")
    num=int(input("enter a num from 1 to 10: "))
print(f"Yes {num} is between 1 to 10")
