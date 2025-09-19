class stud:
    def __init__(self, a ,b, c, m1, m2, m3):
        self.sno = a
        self.sname = b
        self.sage = c
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3
        self.tot = 0
        self.avg = 0
        self.result = ""
    
    def calculate(self):
        self.tot = self.mark1 + self.mark2 + self.mark3
        self.avg = self.tot / 3
        print("total marks =", self.tot)
        print("average =", self.avg)
        if self.mark1 >= 40 and self.mark2 >= 40 and self.mark3 >= 40:
            self.result = "pass"
        else:
            self.result = "fail"
    
    def display(self):
        print("student no:", self.sno)
        print("student name:", self.sname)
        print("student age:", self.sage)
        print("mark1 =", self.mark1)
        print("mark2 =", self.mark2)
        print("mark3 =", self.mark3)
        print("total =", self.tot)
        print("average =", self.avg)
        print("result =", self.result)

# Input section remains the same
x = int(input("enter roll no: "))
y = input("Enter name: ")
z = int(input("Enter age: "))
m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
m3 = int(input("Enter mark3: "))

obj = stud(x, y, z, m1, m2, m3)
obj.calculate()
obj.display()
