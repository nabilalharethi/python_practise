""" The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / . """

a = int(input("Enter a number: "))

b = int(input("Enter a number: "))

int_dev = a//b
float_dev = a/b

print(f"{int_dev}\n{float_dev}")
