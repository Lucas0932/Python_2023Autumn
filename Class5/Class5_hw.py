class Names:
    def __init__(self, name):
        self.name = name
        self.next = None
class Ages:
    def __init__(self, age):
        self.age = age
        self.next = None
Amyname = Names("Amy")
Amyage = Ages("25")
Eddyname = Names("Eddy")
Eddyage = Ages("43")
Esmename = Names("Esme")
Esmeage = Ages("32")
namehead = Amyname
Amyname.next = Eddyname
Eddyname.next = Esmename
agehead = Amyage
Amyage.next = Eddyage
Eddyage.next = Esmeage
def traverse(namehead, agehead):
    nameptr = namehead
    ageptr = agehead
    while nameptr != None:
        print("The employee name is", nameptr.name, "and the age is", ageptr.age, ".")
        nameptr = nameptr.next
        ageptr = ageptr.next

traverse(namehead, agehead)
print("Finish traverse!")