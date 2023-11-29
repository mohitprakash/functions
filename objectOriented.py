
class car():

    wheels = 4

    def __init__(self,Vehicle, Type):
        self.make = Vehicle
        self.T = Type
        #print(self.make)
        #print(self.T)


    def new(self):
        print("My car is " + self.make)


c1 = car("BMW", "SUV")
print(c1.new())
print(c1.wheels)
c1.wheels = 3
print(c1.wheels)

print(car.wheels)

c2 = car("AUDI", "SUV")
print(c2.wheels)

print("Hello Object Oriented")
