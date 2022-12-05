class employee:
    def __init__(self,n,s,a):    
        self.name=n
        self.salary=s
        self.__age=a

    def disp(self):
        print("Name=",self.name)
        print("salary=",self.salary)
        print("Age=",self.__age)
emp1=employee("SUN",2000,65)
emp1.disp()
print(emp1.name)
print(emp1.salary)
print(emp1._employee__age)#to access private members directly
#print(emp.__age) #can not access private members
