a = [1, 2, 3, 4, 5, 6, 7]
print(a[0])
print(a[-1])
print(a[0:3])
a.insert(4, "Mohit")
print(a)

a.append('END')
print(a)

del a[0]
print(a)

b = (1,2,3,4,5)
print(b)

print(b)

# Dictionary data type

a= {1:"SBI",2: "BANK", 3: "American",4: "deutsche" }
print(a)

a[2] = 'NORTHWIND'

print(a.values())

print(a[3])

b = {"a":1, 2:"bcd"}
print(b["a"])
print(b[2])

b = 'Hello World'
if b == "Hello World":
    print("Not Match")
    print("If loop is executed")
else:
    print("match")
    print("Else is executed")

print("if else code is compelted")



# For loop

for i in range(1, 11):
    b = 2*i
    print("2 *", i, "=", b)

#for k in range(1, 10, 4):
#    print(k)

for j in range(10,4):
    print(j)

print("********SKIPPING FIRST INDEX************")

for k in range(1, 10, 2):
    print(k)


print("****************WHILE LOOP****************")
t = 10
while t > 1:
    if t == 9:
        t = t-1
        continue
    if t == 3:
        break

    print(t)

    t = t-1

print("WHILE LOOP Execution is DONE")



count = 0
while count < 5 :  count = count+1;  print("Hello Count")


m = [1,2,3,4,5,6]
print(*m)

print("*************FUNCTIONS********************")

def HI(name):
    print("HI", name)

HI("MOHIT PRAKASH")

def add_integer(a, b):
    return a+b

print(add_integer(2, 3))