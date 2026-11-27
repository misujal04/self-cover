class bank :
    def __init__(self, bank_name,acc_num ):
        self.Bank_Name = bank_name
        self.acc_num  = acc_num
        self.Total_Amount =  0
    def set_pin(self):
        self.set_pin = int(input("Enter yoour pin in only numbers :"))

    def operation(self):
        self.pin_num= int(input("please Enter Your Pin Number which you have set: \n" ))
        # self.pin_num = 1000
        if self.pin_num == self.set_pin:
            print("type 1 for withdraw ")
            print("Type 2 for Deposit ")
            i = int(input("Enter your choice\n"))
            if i == 1 :
                # self.withdraw()
                c1.withdraw()
            elif i == 2 :
                self.deposit()
                c1.deposit()
        else:
            print("You have Entered a Wrong pin" )
    def deposit(self):
         
         self.Deposit = float(input("Enter Your Amount of your Money : "))
         self.Total_Amount = self.Deposit + self.Total_Amount 
         print("Your Account Has Succesfully Updated Here is Your Current balance :", self.Total_Amount)


    def withdraw (self):
        
        self.withdraw_amnt = float(input("Enter How much Amount do You Want to withdraw "))
        if self.withdraw_amnt < self.Total_Amount :

            self.Total_Amount = self.Total_Amount - self.withdraw_amnt

            print("Your Amount have successfullu withdrawn  and current Balance is : ", self.Total_Amount)
        elif self.withdraw_amnt == 0 :
            print("You can not withdraw o ")
        else:
            print("Insufficient balance")



    def Accdetails(self):
        # c ="Bank Name :" , self.Bank_Name
        # b = "Account Number : ", self.acc_num 
        # return print(c)
        print("Bank Name : ", self.Bank_Name )
        print("Account Number :",self.acc_num)


c1 = bank("Union Bank ", 4644834)
c1.set_pin()
c1.operation()

# c1.Accdetails()
    
    
    