s=(lambda x:x*x)
print(s(3))


def add(a,b):
    print("Addition",a+b)
    print("Multiplication",a*b)
    print("Division",a/b)
    print("Substraction",a-b)

add(40,20)

op=input("Enter op:")
if(op=="+"):
    s=lambda a,b:a+b
    print(s(10,20))
elif(op=="-"):
    s=lambda a,b:a-b
    print(s(20,10))
elif(op=="*"):
    s=lambda a,b:a*b
    print(s(20,10))
elif(op=="/"):
    s=lambda a,b:a/b
    print(s(20,10))