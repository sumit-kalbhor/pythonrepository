
class Employee:
    # instance method in python
    def employeeDetails(self):
        self.name = "Sumit"
        print("Employee name is " + self.name)

# static method in python

    @staticmethod
    def welcome():
        print("Welcome to organization")


# creating an object of class
employee = Employee()

# calling a methods from class using object
employee.employeeDetails()
employee.welcome()
