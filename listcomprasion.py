# import sys
# x=(i**2 for i in range(10))
# print(sys.getsizeof(x))
# print(x)

# x=(i**2 for i in range(10))
# greet=x
# print(next(greet))
# print(next(greet))
# print(next(greet))
# for i in range(7):
#     print(next(greet))



# def greet():
#     for i in range(10):
#         c=i**2
#         yield c

# gen=greet()
# print(next(gen))

    

# def greet(*a):
#     for i in range(a[0],a[1],a[2]):
#         yield i
# gen=greet(20,10,-1)
# for i in gen:
#     print(i)

# gen=greet(10,20,-1)
# for i in gen:
#     print(i)

# def even(a):
#     for i in range(1,a+1):
#         if i%2==0:
#             yield i
# gen=even(10)
# print(next(gen))

# def cube(a):
#     for i in range(1,a):
#         j=a**3
#         yield i 

# print(next(cube(10)))


# def table(a):
#     for i in range(1,11):
#         total=a*i
#         yield total
# gen=table(3)
# for i in gen :
#     print(i)


