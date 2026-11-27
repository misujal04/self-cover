import time
# def task1():
#     print("Task1 started")
#     time.sleep(2)
#     print("Task1 completed")

# def task2():
#     print("Task2 started")
#     time.sleep(2)
#     print("Task1 completed")

# task1()
# task2()
# import threading
# def greet1():
#     time.sleep(3)
#     print("Hello from the thread 1st")
    
# def greet2():
#     time.sleep(5)
#     print("\nHello from the thread 2nd")
# def greet3():
#     print("Hello from the thread 3rd")
# t1=threading.Thread(target=greet1)
# t2=threading.Thread(target=greet2)
# t3=threading.Thread(target=greet3)
# t1.start()
# t1.join()
# t2.start()
# t3.start()
# print("\nMain program")


# import threading
# def greet(name,age):
#     print("Hello","\nname is ",name,"\nage is ",age)

# t1=threading.Thread(target=greet, args=(age:=19,name:="Aarav"))
# t1.start()
# t1.join()


import threading
counter=0
def increase_counter():
    global counter
    for _ in  range(100000):
        counter+=1
t1=threading.Thread(target=increase_counter)
t2=threading.Thread(target=increase_counter)

t1.start()
t2=start()
