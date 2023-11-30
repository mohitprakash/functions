class car():
    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started....")

    def stop(self):
        print("Car stopped")

class BMW(car):

    def __init__(self):
        car.__init__(self)
        print("You just create the BMW instance")


#c = car()
#c.drive()
#c.stop()

b = BMW()
b.drive()
b.stop()


