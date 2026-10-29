a=int(input("Enter a number"))
b=int(input("Enter a number"))
print("a=", a)
print("b=", b)
a,b = b,a
print("a=", a)
print("b=", b)

OUTPUT
Enter a number3
Enter a number5
a= 3
b= 5
a= 5
b= 3
