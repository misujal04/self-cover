# print("sujal")
# n=int(input("enter the number"))
# print(n)
# print(type(n))

# b=range(1,1000)
# i=b
# print(i in b)
# for i in b:
#     print (i)

# b=range(65,90)

# for i in sorted(b,reverse=True):
#     print (chr(i))
# print(sorted(b,reverse=True))


# a=[40]
# b=50
# c=0
# print(sum(a,b))

# def student(name, age=22):
#     print(name)
#     print(age)

# student("Sujal",55)
x=10
def show():
    nonlocal x
    x=20
    def inner():
        nonlocal x
        x=30
    inner()
    print(x)
show()
print()
