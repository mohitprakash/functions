print("***********\"LIST METHODS\" ******************")

cars = ["bmw", "honda", "audi"]

print(cars)
print(cars[0])

num_list = [1, 2, 3]
sum_num = num_list[2] + num_list[1]
print(sum_num)

more_cars = ["bmw", "honda", "audi"]
more_cars[1] = "Benz"
print(more_cars)

print("************************\"APPEND METHODS\"********************")

more_cars.append("honda")
print(more_cars)

print("************************\"INSERT METHODS\"********************")

more_cars.insert(1, 'Jeep')
print(more_cars)

print("************************\" GIVE THE INDEX METHODS\"********************")

x = more_cars.index("audi")
print(x)

print("************************\" POP METHODS\"********************")

x = more_cars.pop()
print(x)
print(more_cars)

print("************************\" REMOVE METHODS\"********************")
more_cars.remove("Jeep")
print(more_cars)

print("************************\" SORT METHODS\"********************")
more_cars.sort()
print(more_cars)

