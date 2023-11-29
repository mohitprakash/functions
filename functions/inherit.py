class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printName(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printName()


class Emp(Person):
    def Print(self):
        print("Emp class calling")


y = Emp("Mohit", "Prakash")
y.printName()

y.Print()

