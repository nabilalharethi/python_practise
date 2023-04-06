
Age = float(input("Enter Age, enter months Like this (1.4): "))

if Age <= 1 and Age >0:
    print("This person is an infant")
elif Age > 1 and Age <= 13:
    print("This person is a child")
elif Age > 13 and Age < 18:
    print("This is a teenager")
elif Age >= 18:
    print("This person is an adult")
elif Age < 0:
    print("invalid age")