

class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age
head = Car("Amy", "25")

def traverse(head):
    ptr = head
    while ptr != None:
        print("The employee name is", ptr.name, "and the age is", ptr.age, ".")
        print("Finish traverse!")
        break
traverse(head)