# class Student:
#     def __init__(self,name):
#         self.name = name 
#         self.marks = {} 

# s1 = Student("yogi")
# s1.name = "yogi"
# s1.marks ={ "math":90,
#            "eng":56}

# print (s1.name , s1.marks)

class Account:
    def __init__(self, acc_no, balance):
        self.acc_no=acc_no
        self.balance = balance

    def credit(self):
        b = int(input("Enter the amount  you  want to credit :"))
        self.balance =int( self.balance) + b
        print(self.balance)
    def debit(self):
        c = int(input("Enter the amount  you  want to debit :"))
        self.balance =int( self.balance) -c
        print(self.balance)


a1 = Account(1,1000)
print(a1.balance)
a1.credit()