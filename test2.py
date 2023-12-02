op=input("enter op(+,-,*,/):")
a=int(input('enter a:'))
b=int(input("enter b:"))
if op == "+":
    print(a+b)
if op == "-":
    print(a-b)
if op == "*":
    print(a*b)
if op == "/":
    if b == 0:
        print("no")
    else:
        print(a/b)

