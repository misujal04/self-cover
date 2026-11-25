def add(a,b,c=10):
    return a+b+c

x=lambda x,y: add(x,y)
print (x(1,2))