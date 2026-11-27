# class Student:
#     def display(self,name,age,course):
#         print("Name is ",name)
#         print("Age is ",age)
#         print("Course is ",course)

# s3=s2=s1=Student()
# s1.display("Sujal",22,"Mca")
# s2.display("Rahul",22,"MBA")
# s3.display("Sonal",59,"cue")

# class Student:
#     def employeedet(self):
#         self.name=input("Enter the Name")
#         self.age=int(input("Enter the age"))
#         self.course=input("Entet the course")

#     def display(self):
#         print("Name is ",self.name)
#         print("Age is ",self.age)
#         print("Course is ",self.course)

# s2=s1=Student()
# s1.employeedet()
# s1.display()
# s2.employeedet()
# s2.display()

# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
# qu2=qu1=Calculator()
# print(qu1.add(2,10))
# print(qu2.sub(10,20))

# class Student:

#     def display(self):
#         print("Hello Student")


# s1 = Student()
# s1.display()

# class Mobile:
#     def info(self):
#         self.brand=input("Enter the value")
#         self.model=input("Enter the model")
#         self.price=input("Enter the price")

#     def display(self):
#         print("Brand name is ",self.brand)
#         print("model name is ",self.model)
#         print("price is ",self.price)  
# s1=Mobile()
# s1.info()
# s1.display()


# class rectangle:
#     def area(self,a,b):
#         return a*b
#     def perimeter(self,a,b):
#         return 2*a+2*b
# s1=rectangle()
# print(s1.area(10,50))
# print(s1.perimeter(10,50))

class BankAccount():
    def info(self):
        self.name=input("Enter the name of Account Holder")
        self.amount=float(input("Enter the amount"))
        print("Account Holder name",self.name)
        print("Account Balance",self.amount)
    def deposit_in(self):
        self.deposit=float(input("Enter the amount"))
        self.amount=self.amount+self.deposit
        print("after deposit",self.amount)
    def withdraw_in(self):
        self.withdraw=float(input("Enter the amount"))
        if self.withdraw>self.amount:
            print("not enough balance")
        else:
            self.amount=self.amount-self.withdraw
            print("after withdraw",self.amount)
    def display_in(self):
        print("Account Holder Name",self.name)
        print("Account blance",self.amount)

s1=BankAccount()
s1.info()
s1.deposit_in()
s1.withdraw_in()
s1.display_in()



    

