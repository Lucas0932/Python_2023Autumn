class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None
first = Employee("Amy", 25)
first.next = None

def traverse(first):
    ptr = first
    while ptr != None:
        print("The employee name is {} and the age is {}.". format(ptr.name, ptr.age))
        ptr = ptr.next

traverse(first)
print("Finish traverse!")