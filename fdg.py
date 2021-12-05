class Employee:
    total_employee = 0
    def __init__(self, name, work_hour):
        self.name = name
        self.work_hour = work_hour
    def __str__(self):
        s = "Department: " + self.name + ", Work hours: " + str(self.work_hour)
        return s
class FullTimeEmployee(Employee):  # FullTimeEmployee inherited from Employee
    def __init__(self, name, work_hour):
        super().__init__(name, work_hour)  # got access to all parent class attributes
        self.name = name
        self.work_hour = work_hour
    def addFullTimeEmployee(self, A, B, C, D, E, F):  # Names are A,C,E and their respective Work Hours are B,D,F
        self.total_employee = 3  # Child Class' variable total_employee initialized with a value of 3
        Employee.total_employee = Employee.total_employee + self.total_employee  # total_employee of Employee class updated
        print("Full time employees in", self.name, " have to work ", self.work_hour, " hours")
        print("=================================")
        print("=================================")
        print("Department: ", self.name, ",Work Hours :", self.work_hour)
        print("Total employee(s):", self.total_employee)
        print("Employee Details:")
        print("Name: ", A, ", Work hours Remaining:",(self.work_hour - B))  # Total Work_hour - Work_hour of the employee
        print("Name: ", C, ", Work hours Remaining:", (self.work_hour - D))
        print("Name: ", E, ", Work hours Remaining:", (self.work_hour - F))
class PartTimeEmployee(Employee):  # PartTimeEmployee inherited from Employee
    def __init__(self, name, work_hour):
        super().__init__(name, work_hour)  # got access to all parent class attributes
        self.name = name
        self.work_hour = work_hour
    def addPartTimeEmployee(self, A, B, C, D):  # Names are A,C and their respective Work Hours are B,D
        self.total_employee = 2  # Child Class' variable total_employee initialized with a value of 2
        Employee.total_employee = Employee.total_employee + self.total_employee  # total_employee of Employee class updated
        print("Full time employees in", self.name, " have to work ", self.work_hour, " hours")
        print("=================================")
        print("=================================")
        print("Department: ", self.name, ",Work Hours :", self.work_hour)
        print("Total employee(s):", self.total_employee)
        print("Employee Details:")
        print("Name: ", A, ", Work hours Remaining:",(self.work_hour - B))  # Total Work_hour - Work_hour of the employee
        print("Name: ", C, ", Work hours Remaining:", (self.work_hour - D))


p1 = FullTimeEmployee("Finance", 40)
print("=================================")
p1.addFullTimeEmployee("Bob", 12, "Carol", 18, "Mike", 15)
print("=================================")
print(p1)
print("=================================")
p2 = PartTimeEmployee("Others", 25)
print("=================================")
p2.addPartTimeEmployee("David", 12, "Simon", 18)
print("=================================")
print(p2)
print("=================================")
print("Total Employee ", Employee.total_employee)
