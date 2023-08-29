# create a class
class Employee:
    name = "Sumit Kalbhor"
    designation = "Associate I"

    # method
    def grade(self):
        if self.designation == "Associate I":
            print("Grade belongs to A")
        else:
            print("Not belongs to A grade")


# object creation
employeeOne = Employee()

# calling a method from class
employeeOne.grade()


