name=input("enter your name :").strip()
while name=="":
    print("you not enter your name ")
    name=input("enter your name :").strip()
print(f"welcome {name}")
#strip() remove extra spaces from input
