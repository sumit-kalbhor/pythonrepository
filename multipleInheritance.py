
class OperatingSystem:
    multitasking = True


class Hp:
    website = "www.hp.com"


class EliteBook(OperatingSystem, Hp):

    def details(self):
        if self.multitasking is True:
            print("This is a multitasking system. Visit {} for more details".format(self.website))


eliteBook = EliteBook()
eliteBook.details()
