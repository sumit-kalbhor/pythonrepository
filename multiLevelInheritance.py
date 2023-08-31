# Multilevel Inheritance

class Name:
    name = "Sumit Kalbhor"


class Salary(Name):
    salary = 25000


class EmployeeDetails(Salary):
    def __init__(self):
        self.designation = "Associate I"
        print("Employee name is {}. Salary is {} and designation is {}.".format(self.name, self.salary, self.designation))


employeeDetails = EmployeeDetails()
