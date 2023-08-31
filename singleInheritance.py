# Parent Class
class Hp:
    manufacturer = "HP Inc."
    contact = "www.hp.com/contactus"

    def contactDetails(self):
        print("Contact us on : ", self.contact)


# Child class
# able to inherits properties of parent class
class EliteBook(Hp):

    def __init__(self):
        self.yearOfManufacture = 2023

    def manufacturerDetails(self):
        print("This laptop was manufactured in {} by {}".format(self.yearOfManufacture, self.manufacturer))


# Object creation
eliteBook = EliteBook()
eliteBook.manufacturerDetails()
eliteBook.contactDetails()
