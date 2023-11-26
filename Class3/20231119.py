a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
c = int(input("enter number 3:"))
arg = [a, b, c]
num = 0
for i in range (3):
    num += arg[i]
print("First person is", a, "kg.")
print("First person is", b, "kg.")
print("First person is", c, "kg.")
print("------------------------")
print("Total weight is", num, "kg.")